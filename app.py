# app.py
from flask import Flask, render_template, request, jsonify
from codify import code_generator
from helpers import Helpers
import json
import re

codgen = code_generator()
help_me = Helpers()
global_llm = 'gemini'
codgen_chain = codgen.code_generator_chain(global_llm)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    global global_llm,codgen_chain
    user_message = request.form.get('user_message')
    llm = request.form.get('llm')
    if llm!=global_llm:
        codgen_chain = codgen.code_generator_chain(llm)
        global_llm = llm
    language = request.form.get('language')
    
    user_message +=user_message+', use '+language+' language, if i am asking you to generate code, otherwise just answer the question as best of your knowledge'

    try:
        chain_response = codgen_chain.invoke({"user_query": user_message})
        chain_reply = chain_response['text']
    except:
        chain_reply = "Oops! A problem occurred while generating your response from "+llm+", Please try again!"
    
    #get last 10 feedback
    feedback_path = './codify_feedback.json'
    with open(feedback_path, 'r') as file:
        data = json.load(file)
    last_10_feedback = data[-10:]
    
    return jsonify({'user_message': user_message, 'api_response': chain_reply,'last_10_feedbacks':last_10_feedback})

@app.route('/send_feedback', methods=['POST'])
def send_feedback():
    print("in send_feedback backend")
    feedback = request.form.get('feedback')
    feedback_text = request.form.get('feedback_text')
    user_message = request.form.get('user_message')
    api_response = request.form.get('api_response')

    saved = help_me.save_feedback_object(user_message,api_response,feedback,feedback_text)
    
    return jsonify({'status': 'Feedback received', 'feedback_saved':saved})


@app.route('/run_code', methods=['POST'])
def run_code():
    print("run code called")
    code = request.form.get('this_code')
    output = {}
    try:
        code_blocks = re.findall(r'`python[\s\S]+?`', code, flags=re.DOTALL)
        if len(code_blocks)>0:
            code_block = code_blocks[0]  # Extract first match
        else:
            code_blocks = re.findall(r'`[\s\S]+?`',code, flags=re.DOTALL)
            if len(code_blocks)>0:
                code_block=code_blocks[0]
            else:
                return jsonify({'status': 'Data received','output':'Oops! Code not found.'})
        code_block = code_block.replace('python','').replace('`','')
        # Create a dictionary to store local variables
        local_vars = {}

        # Execute the code string with locals() dictionary
        exec(code_block, globals(), local_vars)

        return jsonify({'status': 'Data received','output':"Executed successfully!"})
    except Exception as e:
        return jsonify({'status': 'Data received','output': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)

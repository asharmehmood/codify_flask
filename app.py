# app.py
from flask import Flask, render_template, request, jsonify
from codify import code_generator
from helpers import Helpers
import json

codgen = code_generator()
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
        global_llm=llm
    language = request.form.get('language')
    
    user_message +=user_message+', use '+language+' language, if i am asking you to generate code, otherwise just answer the question as best of your knowledge'

    try:
        chain_response = codgen_chain.invoke({"user_query": user_message})
        chain_reply = chain_response['text']
        # print("----memory")
        # print(codgen_chain.memory)
        # print("memory------")
        # codgen_chain.memory.save_context({"user_query": user_message}, {"you": chain_reply})
    except:
        chain_reply = "Oops! A problem occurred while generating your response from "+llm+", Please try again!"
    
    #get last 10 feedback
    feedback_path = './codify_feedback.json'
    with open(feedback_path, 'r') as file:
        data = json.load(file)
    last_10_feedback = data[-10:]
    print("------------ last 10 feedback ----------------------")
    print(last_10_feedback)
    print("---------------- ended ------------------")
    return jsonify({'user_message': user_message, 'api_response': chain_reply,'last_10_feedbacks':last_10_feedback})

@app.route('/send_feedback', methods=['POST'])
def send_feedback():
    print("in send_feedback backend")
    feedback = request.form.get('feedback')
    feedback_text = request.form.get('feedback_text')
    user_message = request.form.get('user_message')
    api_response = request.form.get('api_response')
    # api_response = ""
    # user_message = ""
    help_me = Helpers()
    saved = help_me.save_feedback_object(user_message,api_response,feedback,feedback_text)
    
    return jsonify({'status': 'Feedback received', 'feedback_saved':saved})

if __name__ == '__main__':
    app.run(debug=True)

# Codify - Your Coding Assistant

Welcome to Codify, your one-stop shop for generating code snippets and tackling coding challenges! This application harnesses the power of cutting-edge language models to deliver accurate and helpful responses to your programming needs.

## Features

* **Multi-Language Support:** Codify understands and works with various programming languages, including Python, JavaScript, and R. Choose your preferred language from the control panel with ease.
* **Language Model Switching:** Customize your experience by selecting between Mistral and Gemini language models. Each model boasts unique strengths, so experiment to find the one that suits you best.
* **Real-Time Code Generation:** Frame your coding questions thoughtfully, and Codify's AI model will interpret them and generate relevant code examples in real-time.
* **Feedback System:** Help shape Codify's evolution by providing feedback on the generated responses. This feedback directly contributes to improving the application's accuracy and effectiveness. The control panel displays the last 10 feedback entries for your reference.
* **Snippet Management System:** Helps you manage all the response from the codify. View any response from the history
and delete unwanted snippets.
* **Snippet Testing System:** Helps you see if code is correct or not (python).

## Local Setup
Clone the repository
```Terminal
git clone https://github.com/asharmehmood/codify_flask.git
cd codify
```
Install the requirements.txt file. (Python=3.10)
```Terminal
pip install -r requirements.txt
```
Run the app
```Terminal
python app.py
```

## Docker Setup
Build the docker image
```Terminal
cd codify
sudo docker build -t codify_flask .
```
Run docker container
```Terminal
sudo docker run codify_flask
```

## How to Use

**1. Select Your Language and LLM:**

- Utilize the control panel on the left side to choose your preferred programming language and language model (LLM). Be aware that switching LLMs will reset your current chat history.

**2. Enter Your Query:**

- Type your coding-related question in the message input box and hit "Send."

**3. Receive Response:**

- Codify will generate a response containing a code snippet or relevant information tailored to your specific query.

**4. Feedback Option:**

- After receiving a response, express your opinion using the thumbs-up or thumbs-down emoji buttons. You can also provide more detailed feedback if desired.

**5. View Last 10 Feedbacks:**

- Click the "Show Feedback" button to view the last 10 feedback entries. This can offer valuable insights into how others interact with Codify.

**6. View and Delete Any Previous Snippet:**

- Go back to history by scrolling and see any snippet. Delete any unwanted snippet from the history.

**7. Test any Snippet:**

- Run current or any previous snippet to see if it is actually working or not.

## Feedback and Contributions

Your feedback is vital for Codify's continuous improvement. If you encounter any problems or have suggestions to enhance its capabilities, please utilize the dedicated feedback feature within the application.

We also welcome contributions to Codify's development. Feel free to submit pull requests or report issues on the GitHub repository (link to be added when available).

We appreciate your interest in Codify!




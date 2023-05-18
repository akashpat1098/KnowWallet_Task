from flask import Flask, render_template, request ,jsonify
import openai
from decouple import config
app = Flask(__name__)

OPENAI_APIKEY = config("OPENAI_API_KEY")
openai.api_key = OPENAI_APIKEY
# starting page of app
@app.route('/')
def home():
    return render_template('index.html')
# ye callback h ,chatgpt prompt ke liye
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    question = data['question']
    
    answer = chat_gpt(question)
    
    return jsonify({'answer': answer})

# chatgpt ko call karne ka function
def chat_gpt(question):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt='Question: ' + question + '\nAnswer:',
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()
# entry point of app
if __name__ == "__main__":
  app.run(debug=True)

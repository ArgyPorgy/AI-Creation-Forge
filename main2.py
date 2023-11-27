from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        gpt_response = response['choices'][0]['message']['content']
        return gpt_response
    except Exception as e:
        print(f"Error during API call: {e}")
        return "Failed to get a response from the GPT model."

if __name__ == '__main__':
    app.run(debug=True,port = 8000)

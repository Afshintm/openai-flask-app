import os
from flask import Flask, request, render_template, jsonify
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            user_prompt = request.form.get('prompt', '')

            response = openai.ChatCompletion.create(
                # model="o3-mini",
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_prompt}
                ]
                # ,
                # reasoning_effort = 'high'
            
            )

            ai_response = response.choices[0].message['content']
            return jsonify({'response': ai_response})

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
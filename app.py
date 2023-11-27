import openai

# Set your OpenAI API key
openai.api_key = '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'

def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful math tutor assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error during API call: {e}")
        return "Failed to get a response from the GPT model."

def math_tutor():
    print("Math Tutor Assistant: Hello! I can help you with basic math operations.")
    
    while True:
        try:
            user_input = input("You: ")

            if user_input.lower() == 'exit':
                print("Math Tutor Assistant: Goodbye!")
                break

            # Send user input to GPT model
            gpt_response = get_gpt_response(user_input)

            print(f"Math Tutor Assistant: {gpt_response}")

        except Exception as e:
            print(f"Math Tutor Assistant: An error occurred: {e}")

if __name__ == "__main__":
    math_tutor()

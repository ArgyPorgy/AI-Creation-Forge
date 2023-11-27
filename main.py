import openai


openai.api_key = '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'

def get_gpt_response(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    

def main():
    while True:
        user_input = input("User: ")
        print("gpt:")
        
        gpt_response = get_gpt_response(user_input)
        print(gpt_response)


if __name__ == "__main__":
    main()

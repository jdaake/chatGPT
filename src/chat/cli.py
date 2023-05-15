import openai

openai.api_key = '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'


def main():
    """
    Function Name: ask_question()

    Description:
    The function "ask_question()" is designed to ask a question to the user and receive a response in the form of a string.

    Syntax:
    def ask_question()

    Parameters:
    The function "ask_question()" does not take any parameters.

    Return Value:
    The function "ask_question()" returns a string, which is the response provided by the user to the question asked.
    """
    messages = []
    while True:
        try:
            question = input('You: ')
            messages.append({'role': 'user', 'content': question})
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500
            )
            messages.append(res['choices'][0]['message'].to_dict())
            print(f"Assistant: {res['choices'][0]['message']['content']}")
        except KeyboardInterrupt:
            print('Exiting...')
            break

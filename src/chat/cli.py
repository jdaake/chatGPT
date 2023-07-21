import openai
import os
from termcolor import colored

openai.api_key = ''
# openai.api_key = os.environ['OPENAI_API_KEY']


def main():
    """
    Function Name: main()

    Description:
    The function "main()" is designed to ask a question to the user and receive a response in the form of a string.

    Syntax:
    def main()

    Parameters:
    The function "main()" does not take any parameters.

    Return Value:
    The function "main()" returns a string, which is the response provided by the user to the question asked.
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
            print(
                colored(f"ChatGPT: {res['choices'][0]['message']['content']}", color='green'))
        except KeyboardInterrupt:
            print('...Exiting...')
            break

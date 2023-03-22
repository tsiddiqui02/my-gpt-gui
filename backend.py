import openai
import os


class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv('API_TOKEN')

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0  # lower it is, more accurate but less diverse in answer
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response()
    print(response)

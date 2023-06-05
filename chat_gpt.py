import openai
import processing_algorithms
from utils import Utils
import settings


class ChatGPT:
    def __init__(self):
        self.openai_api_key = settings.OPENAI_API_KEY

    def get_data_from_research_paper_based_on_feature(self, content):
        content = "what is the conclusion from the research " + processing_algorithms.article_summerization(content,
                                                                                                            0.02)
        openai.api_key = self.openai_api_key
        # model_engine = "text-davinci-002"
        # # Generate a response
        # completion = openai.Completion.create(
        #     engine=model_engine,
        #     prompt=content,
        #     max_tokens=2048,
        #     n=1,
        #     stop=None,
        #     temperature=0.5,
        # )
        #
        # response = completion.choices[0].text
        # return response

        messages = [{"role": "system", "content": "You are a intelligent assistant."},
                    {"role": "user", "content": content}]
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        return reply
        # print(reply)


# print(ChatGPT().get_data_from_research_paper_based_on_feature())

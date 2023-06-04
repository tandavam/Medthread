import PyPDF2
import openai
# from chatgpt_wrapper import ChatGPT


from utils import Utils
class ChatGPT:
    def __init__(self):
        self.openai_api_key = "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"
        self.messages = [{"role": "system", "content": "You are a intelligent assistant."}]

    def get_data_from_research_paper_based_on_feature(self):
        content = "what is the conclusion from the research " + Utils().read_pdf("/Users/sachinsrinivasan/Development/Medthread/research_papers/40665540.pdf")
        # self.messages.append({
        #     "role": "user",
        #     "content": content
        # })
        # # openai.Completion
        openai.api_key = self.openai_api_key
        # # openai.Completion.create()
        # chat = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo", messages=self.messages
        # )
        # reply = chat.choices[0].message.content
        # print(f"ChatGPT: {reply}")
        # self.messages.append({"role": "assistant", "content": reply})
        model_engine = "code-davinci-002"
        prompt = "Who is the president of the United States"

        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=content,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completion.choices[0].text
        print(response)


ChatGPT().get_data_from_research_paper_based_on_feature()

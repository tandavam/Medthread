import openai
import article_summarization
from utils import Utils
import settings


class ChatGPT:
    def __init__(self):
        self.openai_api_key = settings.OPENAI_API_KEY

    def get_data_from_research_paper_based_on_feature(self):
        content = "what is the conclusion from the research " + article_summarization.summarize(Utils().read_pdf(
            "/Users/sachinsrinivasan/Development/Medthread/research_papers/Cancer - 2000 - Chang - Perineal talc exposure and risk of ovarian carcinoma.pdf"),
            0.05)
        openai.api_key = self.openai_api_key
        model_engine = "text-davinci-002"
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
        return response


ChatGPT().get_data_from_research_paper_based_on_feature()

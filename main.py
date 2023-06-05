from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
import openai
import processing_algorithms


class Medthread:
    def __init__(self):
        # self.search_terms = processing_algorithms.remove_stop_words(user_query)
        pass

    @staticmethod
    def create_research_paper_list_and_summary():
        import os
        files = os.listdir("research_papers")
        return files


print(Medthread().create_research_paper_list_and_summary())

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
import openai
import processing_algorithms


class Medthread:
    def __init__(self, user_query):
        self.search_terms = processing_algorithms.remove_stop_words(user_query)


def build_search_terms(user_query):
    pass

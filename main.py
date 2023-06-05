from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import processing_algorithms
from utils import Utils


class Medthread:
    def __init__(self, question):
        self.user_query = question
        self.preprocessed_user_query = None
        self.search_terms = processing_algorithms.remove_stop_words(self.user_query)
        self.conclusions = list()
        self.research_papers = list()
        self.relevant_papers = list()
        self.create_research_paper_list_and_summary()
        self.transform_algorithm()

    def create_research_paper_list_and_summary(self):
        # import os
        list_of_files = self.listdir_nohidden("research_papers")
        for file in list_of_files:
            self.conclusions.append({
                "conclusion": Utils().read_pdf(file)
            })
            self.research_papers.append(file)

    @staticmethod
    def listdir_nohidden(path):
        import glob
        import os
        return glob.glob(os.path.join(path, '*'))

    def transform_algorithm(self):
        self.preprocessed_user_query = " ".join(self.search_terms)
        for index in range(len(self.conclusions)):
            preprocessed_research_paper_contents = " ".join(self.conclusions[index]["conclusion"].lower().split())
            vectorizer = TfidfVectorizer(stop_words='english')
            query_vector = vectorizer.fit_transform([self.preprocessed_user_query])
            research_vector = vectorizer.transform([preprocessed_research_paper_contents])
            similarity_score = cosine_similarity(query_vector, research_vector)[0][0]
            if similarity_score > 0.6:
                self.relevant_papers.append(index)
        self.return_relevent_research_papers_based_on_user_query()

    def return_relevent_research_papers_based_on_user_query(self):
        if self.relevant_papers:
            for title in self.relevant_papers:
                print("Research Paper Title: ", self.research_papers[title])
        else:
            print("No Papers found")


if __name__ == "__main__":
    query = input("Enter your research question: ")
    Medthread(question=query).return_relevent_research_papers_based_on_user_query


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
import openai

# Step 1: User Query
user_query = input("Enter your research question: ")

# Step 2: Build Search Terms
search_terms = user_query.lower().split()

# Step 3: Build Search Types
search_types = ["case-controlled", "cohort", "randomized controlled trial", "meta-analysis", "systematic review", "cross-sectional", "longitudinal", "observational"]

# Step 4: Create a database of research papers
research_papers = [
    "https://acsjournals.onlinelibrary.wiley.com/doi/epdf/10.1002/%28SICI%291097-0142%2819970615%2979%3A12%3C2396%3A%3AAID-CNCR15%3E3.0.CO%3B2-M",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2247100/pdf/brjcancer00120-0090.pdf",
    "https://onlinelibrary.wiley.com/doi/full/10.1002/ijc.20434",
    "https://acsjournals.onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0142%2819970615%2979%3A12%3C2396%3A%3AAID-CNCR15%3E3.0.CO%3B2-M",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4820665/",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9360263/",
    "https://pubmed.ncbi.nlm.nih.gov/31910280/",
    "https://www.jstor.org/stable/40665540"
]

# Step 5: Key Features Extraction
selected_features = ['conclusion']

# Step 6: Data Extraction
data = [
    {
      "conclusion": "This  investigation  supports  previous  contentions  that  exposure  totalc may increase risk of ovarian carcinoma. Questionable trends in duration andfrequency  of  exposure  suggest  that  further  studies  may  be  needed  to  clarify  therole of talc in the etiology of this disease."
    },
    {
      "conclusion": "Age at first pregnancy was not found to be associated with ovarian cancer risk although women having a first pregnancy after the age of 35 years had a higher risk compared to women having a first pregnancy at earlier ages and to nulligravid women. "
    },
    {
      "conclusion": "Talc use was higher in white non-Hispanics compared to Hispanics in this study. However, the pattern of increased use in EOC cases for both groups contributed to the overall increased risk of EOC among talc users. Differential talc use by various ethnic groups and its relation to EOC risk has not, to our knowledge, been evaluated previously."
    },
    {
      "conclusion": "This investigation supports previous contentions that exposure to talc may increase risk of ovarian carcinoma. Questionable trends in duration and frequency of exposure suggest that further studies may be needed to clarify the role of talc in the etiology of this disease."
    },
    {
      "conclusion": "Risks for epithelial ovarian cancer from genital talc use vary by histologic subtype, menopausal status at diagnosis, HT use, weight, and smoking. These observations suggest that estrogen and/or prolactin may play a role via macrophage activity and inflammatory response to talc."
    },
    {
      "conclusion": "This review suggests an increased risk of ovarian cancer associated with frequent perineal powder exposure of 31–65%."
    },
    {
      "conclusion": "In this analysis of pooled data from women in 4 US cohorts, there was not a statistically significant association between use of powder in the genital area and incident ovarian cancer. However, the study may have been underpowered to identify a small increase in risk."
    },
    {
      "conclusion": "Ovarian cancer is one of the most common gynaecological neoplasms, especially in industrialised countries. The aetiology of the disease is not well understood, except that inherited mutations in the breast cancer genes BRCA-1 and BRCA-2 account for up to 10% of all cases, ¹and child-bearing, oral contraceptive use and breast-feeding reduce the risk. ²Some environmental exposures, notably talc and asbestos, have been suspected as ovarian carcinogens."
    }
]

# Step 7: Relevance Assessment
relevant_papers = []

# Preprocess user query for vectorization
user_query_preprocessed = " ".join(search_terms)

for i in range(len(data)):
    # Preprocess paper content for vectorization
    paper_content_preprocessed = " ".join(data[i]["conclusion"].lower().split())

    vectorizer = TfidfVectorizer(stop_words='english')
    query_vector = vectorizer.fit_transform([user_query_preprocessed])
    paper_vector = vectorizer.transform([paper_content_preprocessed])

    similarity_score = cosine_similarity(query_vector, paper_vector)[0][0]
    if similarity_score > 0.5:  # Adjust the threshold as needed
        relevant_papers.append(i)

# Display the relevant papers
if relevant_papers:
    print("Relevant Papers:")
    for paper_data in relevant_papers:
        print("Research Paper Url: ", research_papers[paper_data])
        print("--------")
else:
    print("No relevant papers found.")



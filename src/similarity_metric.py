from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# function to calculate similarity score
def vectorizerNCosineSim(data1, data2):
    count_vectorizer = CountVectorizer()
    # Calculate cosine similarity score between 2 job titles
    vector_matrix = count_vectorizer.fit_transform([data1,data2])
    return cosine_similarity(vector_matrix)[0][1]


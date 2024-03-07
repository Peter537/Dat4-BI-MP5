import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def get_description_recommendations(df, description):
    try:
        indices, cosine_sim = train_model(df, 'overview')

        idx = indices[description]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        return df.iloc[movie_indices]
    except:
        return "No recommendations found"
    
def get_title_recommendations(df, title):
    try:
        indices, cosine_sim = train_model(df, 'title')

        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        return df.iloc[movie_indices]
    except:
        return "No recommendations found"

def get_recommendations(df, input, column):
    try:
        indices, cosine_sim = train_model(df, column)
        
        idx = indices[input]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        return df.iloc[movie_indices]
    except:
        return "No recommendations found"

def train_model(dataframe, column_name, language='english'):
    print("Training model...")

    tfidf = TfidfVectorizer(stop_words=language)

    dataframe[column_name] = dataframe[column_name].fillna('')

    tfidf_matrix = tfidf.fit_transform(dataframe[column_name])

    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(dataframe.index, index=dataframe[column_name]).drop_duplicates()

    print("Model trained!")

    return indices, cosine_sim

import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(ratings_matrix):
    # Calculate cosine similarity to measure how similar each user is to others
    return cosine_similarity(ratings_matrix)

def recommend_tours(user_id, ratings_matrix, similarity_matrix, tours_data, user_ids, top_n=20):
    # Convert the user_id to a valid index
    user_index = np.where(user_ids == user_id)[0]  # Find the index of the user_id in user_ids
    if len(user_index) == 0:
        raise ValueError(f"User ID {user_id} not found!")
    
    user_index = user_index[0]  # Get the first match, in case there are multiple entries
    
    # Get the similarity scores for the user
    user_similarity_scores = similarity_matrix[user_index]
    
    # Calculate the weighted ratings for each tour based on user similarity
    weighted_ratings = similarity_matrix[user_index].dot(ratings_matrix) / np.abs(user_similarity_scores).sum()  # Normalize scores
    
    # Sort the scores in descending order
    recommended_indices = np.argsort(weighted_ratings)[::-1][:top_n]
    
    # Fetch the details of the recommended tours using the indices
    recommended_tours = tours_data.iloc[recommended_indices]
    
    # Return a list of dictionaries with the tour details (Name, State, etc.)
    return recommended_tours.to_dict(orient='records')

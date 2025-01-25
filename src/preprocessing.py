import pandas as pd

def load_data(user_file, tour_file, rating_file):
    users = pd.read_csv(user_file)
    tours = pd.read_csv(tour_file)
    ratings = pd.read_csv(rating_file)
    return users, tours, ratings

def create_ratings_matrix(ratings):
    return ratings.pivot(index='user_id', columns='tour_id', values='rating').fillna(0)

if __name__ == "__main__":
    users, tours, ratings = load_data(
        "data/raw/users.csv", 
        "data/raw/tours.csv", 
        "data/raw/ratings.csv"
    )
    ratings_matrix = create_ratings_matrix(ratings)
    ratings_matrix.to_csv("data/processed/ratings_matrix.csv", index=False)

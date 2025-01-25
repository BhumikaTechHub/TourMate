from flask import Flask, render_template, request, send_from_directory
import pandas as pd
import numpy as np
from src.recommender import calculate_similarity, recommend_tours
import os

app = Flask(__name__)

# Load the tours dataset with details
tours_data = pd.read_csv("data/raw/tours.csv")

# Ensure the relevant columns are selected
tours_data = tours_data[['DestinationID', 'Name', 'State', 'Type', 'Popularity', 'BestTimeToVisit']]

# Load the ratings matrix
ratings_matrix = pd.read_csv("data/processed/ratings_matrix.csv").values

# Define the user IDs (this should be a list of user IDs corresponding to the rows in the ratings matrix)
user_ids = np.arange(1, ratings_matrix.shape[0] + 1)  # Assuming users are indexed from 1 to N

# Calculate the similarity matrix
similarity_matrix = calculate_similarity(ratings_matrix)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home1():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = int(request.args.get('user_id', 0))  # Default to 0 if no user_id is provided

    # Get the recommended tours with detailed information
    recommendations = recommend_tours(user_id, ratings_matrix, similarity_matrix, tours_data, user_ids)

    # Render the response using HTML and Bootstrap
    recommendation_list = []
    for tour in recommendations:
        recommendation_list.append({
            'Name': tour['Name'],
            'State': tour['State'],
            'Type': tour['Type'],
            'Popularity': tour['Popularity'],
            'BestTimeToVisit': tour['BestTimeToVisit']
        })

    # Return the formatted HTML with Bootstrap styling
    return render_template('recommendations.html', user_id=user_id, recommendation_list=recommendation_list)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

if __name__ == "__main__":
    app.run(debug=True)

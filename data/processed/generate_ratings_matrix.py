import pandas as pd

# Load the reviews or user history dataset
reviews_df = pd.read_csv("ratings.csv")

# Create a pivot table (user-item matrix)
ratings_matrix = reviews_df.pivot_table(
    index='UserID',
    columns='DestinationID',
    values='Rating',  # Replace 'Rating' with 'ExperienceRating' if using the other dataset
    fill_value=0  # Fill missing ratings with 0 or NaN
)

# Save the matrix as a CSV file
ratings_matrix.to_csv("ratings_matrix.csv")

print("ratings_matrix.csv has been generated successfully.")

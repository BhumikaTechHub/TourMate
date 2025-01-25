import unittest
from src.recommender import calculate_similarity, recommend_tours
import numpy as np

class TestRecommender(unittest.TestCase):
    def test_recommend_tours(self):
        ratings_matrix = np.array([[5, 0, 0], [4, 0, 0], [0, 5, 4]])
        similarity_matrix = calculate_similarity(ratings_matrix)
        recommendations = recommend_tours(0, ratings_matrix, similarity_matrix)
        self.assertTrue(len(recommendations) > 0)

if __name__ == '__main__':
    unittest.main()

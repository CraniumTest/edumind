import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, content_repository):
        self.content_repository = content_repository

    def recommend_content(self, user):
        user_interests = self._mock_user_interests(user)
        content_scores = self._assess_content(user_interests)
        recommended_indices = np.argsort(content_scores)[-3:]  # Last 3 items
        return [self.content_repository.get_contents()[i] for i in recommended_indices]

    def _mock_user_interests(self, user):
        interests = np.random.rand(len(self.content_repository.get_contents()))
        return interests

    def _assess_content(self, interests):
        content_matrix = np.random.rand(len(self.content_repository.get_contents()), 5)
        return cosine_similarity([interests], content_matrix)[0]

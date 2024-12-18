import numpy as np

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.performance = {}
        self.engagement = []

    def update_performance(self, subject, score):
        if subject not in self.performance:
            self.performance[subject] = []
        self.performance[subject].append(score)

    def update_engagement(self, activity):
        self.engagement.append(activity)

    def get_performance(self):
        return self.performance

    def get_engagement(self):
        return self.engagement

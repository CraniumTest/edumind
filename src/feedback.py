class FeedbackSystem:
    def __init__(self):
        pass

    def give_feedback(self, performance):
        feedback = {}
        for subject, scores in performance.items():
            last_score = scores[-1]
            improvement = (last_score - np.mean(scores[:-1])) if len(scores) > 1 else last_score
            feedback[subject] = f"Last Score: {last_score}, Improvement: {improvement}"
        return feedback

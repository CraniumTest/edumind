from user import User
from content_repository import ContentRepository
from recommender import Recommender
from feedback import FeedbackSystem

def main():
    # Initialize components
    content_repo = ContentRepository()
    recommender = Recommender(content_repo)
    feedback_system = FeedbackSystem()

    # Load mock content
    mock_contents = ["Math Basics", "Advanced Physics", "Introduction to Biology", "Chemistry 101", "World History"]
    for content in mock_contents:
        content_repo.add_content(content)

    # Create a user
    user = User(user_id=1, name="Alice")

    # Simulate user performance and engagement
    user.update_performance("Math", 80)
    user.update_performance("Math", 85)
    user.update_engagement("Completed Math Basics")

    # Get recommendations
    recommended_content = recommender.recommend_content(user)
    print("Recommended Content:", recommended_content)

    # Provide feedback
    feedback = feedback_system.give_feedback(user.get_performance())
    print("Feedback:", feedback)

if __name__ == "__main__":
    main()

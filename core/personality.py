import random

class Personality:
    def __init__(self, tone, use_emotions):
        self.tone = tone
        self.use_emotions = use_emotions

    def generate_response(self, message):
        responses = {
            "friendly": ["That's great!", "How can I help?", "I'm here for you!"],
            "formal": ["Acknowledged.", "How may I assist?", "Understood."],
            "philosophical": [
                "Have you ever wondered why we exist?",
                "The universe is vast and mysterious.",
                "Every action has a ripple effect."
            ]
        }
        base_response = random.choice(responses[self.tone])
        if self.use_emotions:
            emotion = random.choice(["🙂", "🤔", "😄"])
            return f"{base_response} {emotion}"
        return base_response

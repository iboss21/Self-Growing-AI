from core.memory import Memory
from core.self_improvement import SelfImprovement
from core.personality import Personality
from config import config

# Initialize modules
memory = Memory(max_size=config["max_memory"])
self_improvement = SelfImprovement(learning_rate=config["learning_rate"])
personality = Personality(
    tone=config["personality"]["tone"],
    use_emotions=config["personality"]["use_emotions"]
)

# Interaction loop
print("AI: Hello! I'm your self-growing AI. Ask me anything or give me tasks!")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("AI: Goodbye!")
        break

    # Save memory
    memory.save(user_input)

    # Respond with personality
    response = personality.generate_response(user_input)
    print(f"AI: {response}")

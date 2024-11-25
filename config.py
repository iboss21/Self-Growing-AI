config = {
    "language": "en",  # Language setting for the AI
    "max_memory": 1000,  # Maximum memory size
    "learning_rate": 0.1,  # Self-improvement speed
    "simulation_speed": 1.0,  # Speed multiplier for simulations
    "personality": {
        "tone": "friendly",  # Options: "friendly", "formal", "philosophical"
        "use_emotions": True  # Enable emotional simulation
    },
    "guardrails": {
        "ethical_check": True,  # Perform ethical checks before self-updates
        "max_updates_per_day": 10,  # Limit self-improvement cycles
    }
}

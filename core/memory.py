class Memory:
    def __init__(self, max_size):
        self.max_size = max_size
        self.storage = []

    def save(self, data):
        if len(self.storage) >= self.max_size:
            self.storage.pop(0)  # Remove oldest memory if max size is reached
        self.storage.append(data)

    def recall(self, query):
        results = [item for item in self.storage if query.lower() in item.lower()]
        return results if results else "No relevant memory found."

    def clear_memory(self):
        self.storage = []

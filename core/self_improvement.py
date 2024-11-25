class SelfImprovement:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        self.skills = {}

    def learn(self, skill, feedback):
        if skill not in self.skills:
            self.skills[skill] = 0
        self.skills[skill] += feedback * self.learning_rate
        self.skills[skill] = min(1, max(0, self.skills[skill]))  # Keep within 0-1

    def get_skills(self):
        return self.skills

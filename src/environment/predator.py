class Predator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        self.x += 1  # Simple linear movement

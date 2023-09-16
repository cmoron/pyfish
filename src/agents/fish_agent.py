import math
from physics.potential_fields import compute_forces
from config.settings import ATTRACT_FORCE, REPEL_FORCE

class FishAgent:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Define the maximum speed a fish can move per iteration
        self.MAX_SPEED = 5 

    def update(self, other_fishes, foods, predators):
        fx, fy = compute_forces(self, other_fishes, foods, predators)

        # Calculate the magnitude of the force vector
        magnitude = math.sqrt(fx ** 2 + fy ** 2)

        # Normalize the force vector if it exceeds 1
        if magnitude > 1.0:
            fx /= magnitude
            fy /= magnitude

        # Apply the limited speed
        self.x += fx * self.MAX_SPEED
        self.y += fy * self.MAX_SPEED

        # Ensure the fish remains within the bounds of the screen
        # TODO 800, 600 a configurer
        self.x = min(max(self.x, 0), 800)  # Assuming screen width is 800
        self.y = min(max(self.y, 0), 600)  # Assuming screen height is 600

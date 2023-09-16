import random

from config.settings import ATTRACT_FORCE, REPEL_FORCE
from utils.helpers import distance

MIN_DISTANCE = 10  # Define the minimum distance between fishes to avoid overlap
STRONG_REPEL_FORCE = 5 * REPEL_FORCE  # Stronger repulsion to avoid overlap

def compute_forces(agent, other_fishes, foods, predators):
    fx, fy = 0.0, 0.0

    # Attraction to other fishes
    for fish in other_fishes:
        if fish == agent:
            continue
        d = distance(agent.x, agent.y, fish.x, fish.y)
        if d == 0:
            continue

        f = ATTRACT_FORCE / d
        fx += f * (fish.x - agent.x) / d
        fy += f * (fish.y - agent.y) / d

    # Attraction to food
    for food in foods:
        d = distance(agent.x, agent.y, food.x, food.y)
        if d == 0:
            continue

        f = ATTRACT_FORCE * 2 / d  # Higher attraction towards food
        fx += f * (food.x - agent.x) / d
        fy += f * (food.y - agent.y) / d

    # Repulsion from predators
    for predator in predators:
        d = distance(agent.x, agent.y, predator.x, predator.y)
        if d == 0:
            continue

        f = REPEL_FORCE / d
        fx += f * (agent.x - predator.x) / d
        fy += f * (agent.y - predator.y) / d

    # Add a random force for exploration
    fx += random.uniform(-0.2, 0.2)
    fy += random.uniform(-0.2, 0.2)

    # Strong repulsion to avoid overlap between fishes
    # for fish in other_fishes:
        # if fish == agent:
            # continue
        # d = distance(agent.x, agent.y, fish.x, fish.y)
        # if d < MIN_DISTANCE:  # If distance is less than minimum distance
            # f = STRONG_REPEL_FORCE / (d + 0.1)  # Adding 0.1 to avoid division by zero
            # fx += f * (agent.x - fish.x) / (d + 0.1)  # Adding 0.1 to normalize
            # fy += f * (agent.y - fish.y) / (d + 0.1)  # Adding 0.1 to normalize

    # Repulsion from other fishes to discourage clustering
    for fish in other_fishes:
        if fish == agent:
            continue
        d = distance(agent.x, agent.y, fish.x, fish.y)
        if d < 20:  # Arbitrary distance threshold
            f = REPEL_FORCE / d
            fx += f * (agent.x - fish.x) / d
            fy += f * (agent.y - fish.y) / d

    return fx, fy

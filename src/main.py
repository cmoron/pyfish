#!/usr/bin/env python3

from agents.fish_agent import FishAgent
from environment.food import Food
from environment.predator import Predator
from gui.graphics import draw_environment
from utils.helpers import distance
import pygame
import random

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Fish Swarm Simulation')

    fishes = [FishAgent(x=100+i*10, y=100+i*10) for i in range(30)]
    foods = [Food(x=400, y=300)]
    predators = [Predator(x=700, y=500)]

    predators = []

    clock = pygame.time.Clock()

    running = True

    food_timer = 0
    predator_timer = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update agents
        for fish in fishes:
            fish.update(fishes, foods, predators)

        # Update environment
        for predator in predators:
            predator.update()

        # Check for fish-food collisions and remove eaten food
        for fish in fishes:
            for food in foods:
                # Assume MIN_DISTANCE as the collision distance
                if distance(fish.x, fish.y, food.x, food.y) < 5:
                    foods.remove(food)
                    break  # Assuming one fish can eat only one food per frame

        # Add more food periodically
        food_timer += 1
        if food_timer >= 30:  # Every 300 frames
            new_food = Food(x=random.randint(0, 800), y=random.randint(0, 600))
            foods.append(new_food)
            food_timer = 0

        # Add more predators periodically
        predator_timer += 1
        if predator_timer >= 20:  # Every 600 frames
            # new_predator = Predator(x=random.randint(0, 800), y=random.randint(0, 600))
            new_predator = Predator(x=0, y=random.randint(0, 600))
            predators.append(new_predator)
            predator_timer = 0

        # Draw everything
        draw_environment(screen, fishes, foods, predators)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()

import pygame

def draw_environment(screen, fishes, foods, predators):
    screen.fill((255, 255, 255))

    # Draw fishes
    for fish in fishes:
        pygame.draw.circle(screen, (0, 0, 255), (fish.x, fish.y), 5)

    # Draw food
    for food in foods:
        pygame.draw.circle(screen, (0, 255, 0), (food.x, food.y), 5)

    # Draw predators
    for predator in predators:
        pygame.draw.circle(screen, (255, 0, 0), (predator.x, predator.y), 5)

import pygame
from random import randint


class Food:
    __rect = None

    def __init__(self):
        x = 1
        while x % 10 != 0:
            x = randint(40, pygame.display.get_surface().get_rect().width - 40)
        y = 1
        while y % 10 != 0:
            y = randint(40, pygame.display.get_surface().get_rect().height-40)
        self.__rect = pygame.Rect(0, 0, 15, 15)
        self.__rect.center = (x, y)

    def is_eaten(self, snake_head):
        return self.__rect.colliderect(snake_head)

    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), self.__rect)

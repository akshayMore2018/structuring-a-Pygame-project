from entity import Entity
from config import *
import pygame


class Player(Entity):
    def __init__(self):
        Entity.__init__(self)

    def sketch(self, surface):
        pygame.draw.circle(surface, RED, (WIDTH // 2, HEIGHT // 2), 10)

    def update(self):
        pass

import pygame
import sys


class Game:
    def __init__(self, TITLE, WIDTH, HEIGHT, BG, FPS):
        self.title = TITLE
        self.image = pygame.image.load(BG)
        self.fps = FPS
        self.game_over = False
        self.entity_list = []
        self.width = WIDTH
        self.height = HEIGHT
        pygame.init()
        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        for entity in self.entity_list:
            entity.update()

    def sketch(self):
        for entity in self.entity_list:
            entity.sketch(self.surface)

    def run(self):
        while not self.game_over:
            self.surface.blit(self.image,
                              (self.width / 2 - self.image.get_width() / 2, self.height / 2 - self.image.get_height() / 2))
            self.events()
            self.update()
            self.sketch()

            pygame.display.update()
            self.clock.tick(self.fps)

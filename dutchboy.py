from game import Game
from player import Player
from config import *


class DutchBoy(Game):
    def __init__(self):
        Game.__init__(self, TITLE, WIDTH, HEIGHT, BG, FPS)
        self.player = Player()
        self.entity_list.append(self.player)

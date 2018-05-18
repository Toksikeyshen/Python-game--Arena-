import pygame
from Constants import *
import random
from Projective import *
from Character import *


class Mob(Character):
    def __init__(self, game,name, x_start, y_start, dir, image_pack, speed):
        Character.__init__(self, game, name, x_start, y_start, dir, image_pack, speed)

class Orge(Mob):
    def __init__(self, game ,x_start, y_start, dir):
        self.image_pack = ['data/orge_right(1).png', 'data/orge_down(1).png', 'data/orge_left(1).png',
                           'data/orge_up(1).png']
        Mob.__init__(self,game, 'Orge', x_start, y_start, LEFT, self.image_pack, 0.6)

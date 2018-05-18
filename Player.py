import pygame
from Constants import *
from Projective import *
from Character import *
from Mob import *


class Player(Character):
    def __init__(self, game, name):
        Character.__init__(self, game, name, START_X, START_Y, RIGHT, PLAYER_IMAGE_PACK, PLAYER_SPEED)


    def tick(self):
        if self.state != DEAD:
            self.hp += HP_REG
            self.mp += MP_REG
            if self.hp > MAX_HP:
                self.hp = MAX_HP
            if self.mp > MAX_MP:
                self.mp = MAX_MP
            if pygame.time.get_ticks() > self.spell_casted + 500:
                self.state = ALIVE
            if self.hp <= 0:
                self.kill()

    def shoot_z(self):
        if self.mp >= SKILL_COST and self.state != SHOOT:
            self.mp -= SKILL_COST
            self.state = SHOOT
            self.spell_casted = pygame.time.get_ticks()
            if self.direction == RIGHT:
                self.__shoot__(12, 0)
            elif self.direction == DOWN:
                self.__shoot__(0, 12)
            elif self.direction == LEFT:
                self.__shoot__(-12, 0)
            else:
                self.__shoot__(0, -12)

    def __shoot__(self, x, y):
        self.game.projective.append(Arrow(self.game, self.x+x, self.y+y, self.direction))



    def render_ui(self, screen):
        # Прорисовка ХП и МП
        z = self.hp
        temp = pygame.image.load('data/hp/hp.png').convert_alpha()
        if 100 >= z > 75:
            # screen.blit(pygame.image.load('data/hp/hp_full.png'), (self.x+19, self.y+58))
            screen.blit(temp.subsurface(0, 20, 25, 5), (self.x + 19, self.y + 58))
        if 75 >= z > 50:
            # screen.blit(pygame.image.load('data/hp/hp_75.png'), (self.x + 19, self.y + 58))
            screen.blit(temp.subsurface(0, 15, 25, 5), (self.x + 19, self.y + 58))
        if 50 >= z > 25:
            # screen.blit(pygame.image.load('data/hp/hp_50.png'), (self.x + 19, self.y + 58))
            screen.blit(temp.subsurface(0, 10, 25, 5), (self.x + 19, self.y + 58))
        if 25 >= z > 0:
            # screen.blit(pygame.image.load('data/hp/hp_25.png'), (self.x + 19, self.y + 58))
            screen.blit(temp.subsurface(0, 5, 25, 5), (self.x + 19, self.y + 58))
        if z == 0:
            # screen.blit(pygame.image.load('data/hp/hp_0.png'), (self.x + 19, self.y + 58))
            screen.blit(temp.subsurface(0, 0, 25, 5), (self.x + 19, self.y + 58))
        m = self.mp
        memp = pygame.image.load('data/mp/mp.png').convert_alpha()
        if 100 >= m > 75:
            # screen.blit(pygame.image.load('data/mp/mp_full.png'), (self.x+19, self.y+65))
            screen.blit(memp.subsurface(0, 20, 25, 5), (self.x + 19, self.y + 65))
        if 75 >= m > 50:
            # screen.blit(pygame.image.load('data/mp/mp_75.png'), (self.x + 19, self.y + 65))
            screen.blit(memp.subsurface(0, 15, 25, 5), (self.x + 19, self.y + 65))
        if 50 >= m > 25:
            # screen.blit(pygame.image.load('data/mp/mp_50.png'), (self.x + 19, self.y + 65))
            screen.blit(memp.subsurface(0, 10, 25, 5), (self.x + 19, self.y + 65))
        if 25 >= m > 0:
            # screen.blit(pygame.image.load('data/mp/mp_25.png'), (self.x + 19, self.y + 65))
            screen.blit(memp.subsurface(0, 5, 25, 5), (self.x + 19, self.y + 65))
        if m == 0:
            # screen.blit(pygame.image.load('data/mp/mp_0.png'), (self.x + 19, self.y + 65))
            screen.blit(memp.subsurface(0, 0, 25, 5), (self.x + 19, self.y + 65))

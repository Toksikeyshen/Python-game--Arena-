import pygame
from Constants import *
import random
from Projective import *


class Character:
    def __init__(self, game, name, x_start, y_start, dir, image_pack, speed):
        self.game = game
        # Состояние персонажа
        self.state = ALIVE
        # Направление персонажа
        self.direction = dir
        self.speed = speed
        # Положение персонажа
        self.x = x_start
        self.y = y_start
        self.size = 40
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.blocked = [0,0,0,0]
        self.mooving = [0, 0, 0, 0]
        self.spell_casted = 0
        self.mob_shoot = 0
        # Цикл на прорисовку
        self.image_pack = image_pack
        self.images = []
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []
            i.append(temp.subsurface(0, 0, 63, 64))
            i.append(temp.subsurface(64, 0, 64, 64))
            i.append(temp.subsurface(128, 0, 64, 64))
            self.images.append(i)

    def render(self, screen):
        # Прорисовка персонажа
        screen.blit(self.images[self.direction][self.state], (self.x, self.y))

    def moove(self):
        self.block_check()
        # функция для задания передвижения персонажа
        if self.state != DEAD:
            if self.mooving[RIGHT] == 1 and self.blocked[RIGHT] == 0:
                self.direction = RIGHT
                self.x += self.speed
            if self.mooving[DOWN] == 1 and self.blocked[DOWN] == 0:
                self.direction = DOWN
                self.y += self.speed
            if self.mooving[LEFT] == 1 and self.blocked[LEFT] == 0:
                self.direction = LEFT
                self.x -= self.speed
            if self.mooving[UP] == 1 and self.blocked[UP] == 0:
                self.direction = UP
                self.y -= self.speed

    def block_check(self):
        self.blocked = [0,0,0,0]
        for i in self.game.mobs:
            if self.x != i.x and self.y != i.y:
                self.contact_check(i)
        if self in self.game.mobs:
            self.contact_check(self.game.player)
        if self.x <= 0: self.blocked[LEFT] = 1
        if self.y <= 0: self.blocked[UP] =1
        if self.x >= SCREEN_WIDTH - 56: self.blocked[RIGHT] = 1
        if self.y >= SCREEN_HEIGHT - 56: self.blocked[DOWN] = 1


    def contact_check(self, obj):
        if self.x >= obj.x - obj.size and self.y <= obj.y +obj.size-SIZE_DIF and self.y >=obj.y - obj.size+SIZE_DIF and self.x <=obj.x +SIZE_DIF*2 and obj.state!= DEAD:
            self.blocked[RIGHT] = 1
            self.strike(obj)
            # self.state = SHOOT
            # obj.hp -= 0.1
        if self.x <= obj.x + obj.size + SIZE_DIF and self.y <= obj.y +obj.size - SIZE_DIF and self.y >= obj.y - obj.size + SIZE_DIF and self.x >= obj.x +obj.size - SIZE_DIF*2 and obj.state!= DEAD:
            self.blocked[LEFT] = 1
            self.strike(obj)
            # self.state = SHOOT
            # obj.hp -= 0.1
        if self.y >= obj.y - obj.size and self.x <= obj.x + obj.size - SIZE_DIF and self.x >= obj.x - obj.size + SIZE_DIF and self.y <= obj.y + SIZE_DIF*2 and obj.state!= DEAD:
            self.blocked[DOWN] = 1
            self.strike(obj)
            # self.state = SHOOT
            # obj.hp -= 0.1
        if self.y <= obj.y + obj.size +SIZE_DIF and self.x <= obj.x + obj.size - SIZE_DIF and self.x >= obj.x - obj.size + SIZE_DIF and self.y >= obj.y+obj.size - SIZE_DIF*2 and obj.state!= DEAD:
            self.blocked[UP] = 1
            self.strike(obj)
            # self.state = SHOOT
            # obj.hp -= 0.1
            self.state = ALIVE


    def random_moove(self):
        if self.blocked != [0,0,0,0]:
            self.change_moove(random.randint(0,3))

    def change_moove(self, direction):
        self.mooving = [0, 0, 0, 0]
        if 0<= direction <= 3:
            self.mooving[direction] = 1

    def kill(self):
        self.hp = 0
        self.mp = 0
        self.state = DEAD
        self.game.corpses.append(self)
        if self in self.game.mobs:
            self.game.mobs.remove(self)

    def strike(self, obj):
        if self.state != SHOOT:
            self.state = SHOOT
            self.mob_shoot = pygame.time.get_ticks()
            obj.hp -= 1

        if pygame.time.get_ticks() > self.mob_shoot + 100:
            self.state = ALIVE

    def tick_mob(self):
        if pygame.time.get_ticks() > self.mob_shoot + 500:
            self.state = ALIVE
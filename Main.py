import pygame
import time
from Constants import *
from Projective import *
from Player import *
from pygame.locals import *
from Mob import *


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(self, 'EgorRich')
        self.projective = []
        self.mobs = []
        self.corpses = []
        self.background = pygame.image.load('data/back.jpg')
        self.running = True
        self.count = 0

    def add_orge(self, x, y):
        self.mobs.append(Orge(self, x, y, LEFT))

    def handle_events(self):
        # Обработка всего
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            # Передвижение игрока
            # При нажатии клавиши
            elif event.type == USEREVENT + 1:
                self.player.tick()
            elif event.type == USEREVENT + 2:
                for i in self.mobs:
                    i.random_moove()
            elif event.type == USEREVENT + 3:

                    for i in range(self.count+8):
                        self.add_orge(random.randint(0, SCREEN_WIDTH - 64), random.randint(0, SCREEN_HEIGHT - 64))
                        self.mobs[i].mooving[random.randint(0, 3)] = 1
                    self.count += 1
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    self.player.mooving = [1, 0, 0, 0]
                if event.key == K_DOWN or event.key == K_s:
                    self.player.mooving = [0, 1, 0, 0]
                if event.key == K_LEFT or event.key == K_a:
                    self.player.mooving = [0, 0, 1, 0]
                if event.key == K_UP or event.key == K_w:
                    self.player.mooving = [0, 0, 0, 1]


            # Другие действия игрока
                if event.key == K_SPACE:
                    if self.player.state != DEAD:
                        self.player.kill()
                    else:
                        self.player.state = ALIVE
                if event.key == K_z:
                    self.player.shoot_z()

            # Проверка смены изображений полоски хп
                if event.key == K_h:
                    self.player.hp -= 25
                    if self.player.hp == 0:
                        self.player.state = DEAD
                    if self.player.hp <= 0:
                        self.player.hp = 0
                if event.key == K_j:
                    self.player.hp += 25
                    if self.player.hp >= 0:
                        self.player.state = ALIVE
                    if self.player.hp >= 100:
                        self.player.hp = 100
            # При отжатии
            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_w:
                    self.player.mooving[UP] = 0
                if event.key == K_DOWN or event.key == K_s:
                    self.player.mooving[DOWN] = 0
                if event.key == K_RIGHT or event.key == K_d:
                    self.player.mooving[RIGHT] = 0
                if event.key == K_LEFT or event.key == K_a:
                    self.player.mooving[LEFT] = 0


    def render(self):
        # прорисовка всего что можно
        self.screen.blit(self.background, (0, 0))
        # for i in self.corpses:
        #     i.render(screen)
        self.player.render(screen)
        self.player.render_ui(screen)
        for i in self.mobs:
            i.render(screen)
        for i in self.projective:
            i.render(screen)
        pygame.display.flip()


    def moove(self):
        if self.player.state != DEAD:
            self.player.moove()
        for i in self.projective:
            i.moove()
        for i in self.mobs:
            i.moove()

    def main_loop(self):
        # главынй цикл игрули
        pygame.time.set_timer(USEREVENT + 1, 100)
        pygame.time.set_timer(USEREVENT + 2, 2000)
        pygame.time.set_timer(USEREVENT + 3, 15000)
        for i in range(8):
            self.add_orge(random.randint(0, SCREEN_WIDTH - 64), random.randint(0, SCREEN_HEIGHT-64))
            self.mobs[i].mooving[random.randint(0, 3)] = 1
        while self.running == True:
            self.moove()
            self.render()
            self.handle_events()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)
game.main_loop()

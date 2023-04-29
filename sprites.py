import pygame as pg
import os
from pygame.sprite import Sprite
from settings import *
from random import randint


vec = pg.math.Vector2


class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        # this will change the image of the player
        self.image = pg.image.load('player.jpg').convert_alpha()
        self.image = pg.transform.scale(self.image, (80,120))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
        self.standing = False
        self.death = False
    # This function allows for movement of the main player 
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        # if a is pressed then the player will move to the left
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
        # if d is pressed then the player will move to the right
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
        # if keystate[pg.K_p]:
        #     if PAUSED == False:
        #         PAUSED = True
        #         print(PAUSED)
        #     else:
        #         PAUSED = False
        #         print(PAUSED)
    # ...
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        # if hits:
        self.vel.y = -PLAYER_JUMP
    
    def mob_collide(self):
            hit_list = pg.sprite.spritecollide(self, self.game.enemies, True)
            if hit_list:
                print('i hit a mob')
                self.game.score += 1
                print(self.game.score)
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        

import random

from pico2d import *

class Bullet:
    eat_sound = None
    def __init__(self):
        self.x, self.y = 0, 0
        self.image1 = load_image('laserblue01.png')
        self.speed = 100
        self.life = False
        if Bullet.eat_sound == None:
            Bullet.eat_sound = load_wav('laser1.wav')
            Bullet.eat_sound.set_volume(32)


    def activate(self, player):
        self.x, self.y = player.x,player.y+50
        self.life = True

    def update(self, frame_time):
        if self.y <620:
            self.y += self.speed/5
            self.y+=20
        if self.y >620:
            self.y = 0
            self.x = -50
            self.y += self.speed/5
            self.y-= 20

    def draw(self):
        if(self.life):
            self.image1.clip_draw(0, 0, 20, 30, self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def eat(self, mob):
        self.eat_sound.play()
        pass




class Bullet2:
    eat_sound = None
    def __init__(self):
        self.x, self.y = 0, 0
        self.image1 = load_image('laserRed02.png')
        self.speed = 120
        self.life = False
        if Bullet2.eat_sound == None:
            Bullet2.eat_sound = load_wav('laser2.wav')
            Bullet2.eat_sound.set_volume(32)


    def activate(self, player):
        self.x, self.y = player.x,player.y+50
        self.life = True

    def update(self, frame_time):
        if self.y <620:
            self.y += self.speed/5
            self.y+=20
        if self.y >620:
            self.y = 0
            self.x = -50
            self.y += self.speed/5
            self.y-= 20

    def draw(self):
        if(self.life):
            self.image1.clip_draw(0, 0, 30, 30, self.x-20, self.y)
            self.image1.clip_draw(0, 0, 30, 30, self.x+20, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x - 20, self.y - 10, self.x + 20, self.y + 10

    def eat(self, mob):
        self.eat_sound.play()
        pass
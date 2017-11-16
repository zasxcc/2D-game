import random

from pico2d import *

class BigMob:
    image = 0
    def __init__(self):
        self.x, self.y = random.randint(15, 785), random.randint(500, 1500)
        self.fall_speed = random.randint(200,300)
        if BigMob.image == 0:
            BigMob.image = load_image('enemyBlack1.png')
        self.parent = None

    def update(self, frame_time):
            self.y -= frame_time * self.fall_speed/10


    def draw(self):
        num = 1
        if(num):
            self.image.draw(self.x, self.y)




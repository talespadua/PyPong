__author__ = 'tales.cpadua'
import random


class Bumper():
    def __init__(self, screen_height, pos_x):
        self.pos_x = pos_x
        self.pos_y = screen_height/3
        self.height = screen_height/4
        self.width = 20

        #Since PyGame does not support Key_Pressed, I will implement boolean check
        self.moving_up = False
        self.moving_down = False

    def move_down(self):
        self.pos_y += 15

    def move_up(self):
        self.pos_y -= 15


class Ball():
    def __init__(self, screen_width, screen_height):
        self.radius = 20
        self.pos_x = screen_width/2 - self.radius/2
        self.pos_y = screen_height/2 - self.radius/2

        self.initial_x_pos = screen_width/2 - self.radius/2
        self.initial_y_pos = screen_height/2 - self.radius/2

        self.screen_w = screen_width
        self.screen_h = screen_height

        self.speed_x = 20

        self.size = 10

        direction = random.randrange(0, 2)
        if direction == 1:
            self.speed_x *= -1
        self.speed_y = random.randrange(-10, 10)

    def reset(self):
        self.pos_x = self.initial_x_pos
        self.pos_y = self.initial_y_pos
        direction = random.randrange(0, 2)
        if direction == 1:
            self.speed_x *= -1
        self.speed_y = random.randrange(-10, 10)

    def move_ball(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

    def set_x_speed(self, speed):
        self.speed_x = speed

    def set_y_speed(self, speed):
        self.speed_y = speed
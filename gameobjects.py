__author__ = 'tales.cpadua'
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
        self.pos_y += 10

    def move_up(self):
        self.pos_y -= 10


class Ball():
    def __init__(self, screen_width, screen_height):
        self.radius = 20
        self.pos_x = screen_width/2 - self.radius/2
        self.pos_y = screen_height/2 - self.radius/2

        self.size = 10

        self.speed_x = 5
        self.speed_y = 2
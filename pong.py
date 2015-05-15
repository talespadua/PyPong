__author__ = 'tales.cpadua'

import pygame

from gameobjects import *

class Pong():
    red = (255, 0, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)

    def __init__(self, screen_width, screen_height):
        #init pygame
        pygame.init()

        #screen size
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.game_font = pygame.font.SysFont(None, 25)

        self.running = True

        # create display
        self.game_display = pygame.display.set_mode((self.screen_width, self.screen_height))

        #set fps and clock
        self.fps = 15
        self.clock = pygame.time.Clock()

        #Name of the window
        pygame.display.set_caption("PyPong")

        #Instantiate game objects
        self.bumper_one = Bumper(self.screen_height, 20)
        self.bumper_two = Bumper(self.screen_height, self.screen_width - 40)
        self.ball = Ball(screen_width, screen_height)

    def mainloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.bumper_one.moving_down = True

                    if event.key == pygame.K_UP:
                        self.bumper_one.moving_up = True


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.bumper_one.moving_down = False

                    if event.key == pygame.K_UP:
                        self.bumper_one.moving_up = False


                # handle pause game
                    if event.key == pygame.K_ESCAPE:
                        self.pause_game()

            if self.bumper_one.moving_down:
                if self.bumper_one.pos_y < self.screen_height - self.bumper_one.height:
                    self.bumper_one.move_down()

            if self.bumper_one.moving_up:
                if self.bumper_one.pos_y > 0:
                    self.bumper_one.move_up()


            self.draw_screen()
            pygame.display.flip()
            #Control FPS
            self.clock.tick(20)



    def draw_screen(self):
        self.game_display.fill(self.black)
        self.game_display.fill(self.white, rect=[self.bumper_one.pos_x, self.bumper_one.pos_y,
                                                 self.bumper_one.width, self.bumper_one.height])
        self.game_display.fill(self.white, rect=[self.bumper_two.pos_x, self.bumper_two.pos_y,
                                                 self.bumper_two.width, self.bumper_two.height])

        self.game_display.fill(self.white, rect=[self.ball.pos_x, self.ball.pos_y, self.ball.size, self.ball.size])


    # handle pause situation
    def pause_game(self):
        paused = True
        self.put_message("Game is Paused")
        pygame.display.update()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
            self.clock.tick(30)

    def put_message(self, message):
        pause_text = self.game_font.render(message, True, self.red)
        self.game_display.blit(pause_text, [self.screen_width / 2, self.screen_height / 2])

    def exit_game(self):
        pygame.quit()
        quit()
__author__ = 'tales.cpadua'

import pygame
from gameobjects import *


class Pong():
    red = (255, 0, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)

    def __init__(self, screen_width, screen_height):
        # init pygame
        pygame.init()

        self.new_round = True

        # screen size
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.score_font = pygame.font.SysFont(None, 50)
        self.text_font = pygame.font.SysFont(None, 25)

        self.running = True

        # create display
        self.game_display = pygame.display.set_mode((self.screen_width, self.screen_height))

        #set fps and clock
        self.fps = 30
        self.clock = pygame.time.Clock()

        #Name of the window
        pygame.display.set_caption("PyPong")

        #Instantiate game objects
        self.bumper_one = Bumper(self.screen_height, 20)
        self.bumper_two = Bumper(self.screen_height, self.screen_width - 40)
        self.ball = Ball(screen_width, screen_height)

        self.player_one_points = 0
        self.player_two_points = 0

    def mainloop_sp(self):
        while self.running:
            self.handle_input_sp()
            self.ball.move_ball()
            self.check_boundaries_collision()
            self.check_bumpers_collision()
            self.draw_screen()
            pygame.display.flip()

            if self.new_round:
                 self.wait_input()
                 self.new_round = False
            # Control FPS
            self.clock.tick(20)

    #wait for input to start round
    def wait_input(self):
        pause_text = self.text_font.render("Press SPACE or ENTER to star round", True, self.red)
        self.game_display.blit(pause_text, [self.screen_width / 3, self.screen_height / 2])
        pygame.display.flip()
        while self.new_round:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        return
                    if event.key == pygame.K_ESCAPE:
                        self.exit_game()
            self.clock.tick(10)

    #Check collision with window boundaries
    def check_boundaries_collision(self):
        if self.ball.pos_x < 0:
            self.player_two_points += 1
            self.ball.reset()
            self.reset_bumpers()
            self.new_round = True

        elif self.ball.pos_x > self.screen_width - self.ball.size:
            self.player_one_points += 1
            self.ball.reset()
            self.reset_bumpers()
            self.new_round = True

        if self.ball.pos_y < 0 or self.ball.pos_y > self.screen_height - self.ball.size:
            self.ball.speed_y *= -1

    def reset_bumpers(self):
        self.bumper_one.moving_down = False
        self.bumper_one.moving_up = False
        self.bumper_two.moving_down = False
        self.bumper_two.moving_up = False

    #Check if the ball collide with the bumpers
    def check_bumpers_collision(self):
        if (self.ball.pos_x < self.bumper_one.pos_x + self.bumper_one.width and
                    self.ball.pos_x + self.ball.size > self.bumper_one.pos_x and
                    self.ball.pos_y < self.bumper_one.pos_y + self.bumper_one.height and
                    self.ball.pos_y + self.ball.size > self.bumper_one.pos_y):
            self.ball.speed_x *= -1
            if self.bumper_one.moving_up:
                self.ball.speed_y -= 5
            elif self.bumper_one.moving_down:
                self.ball.speed_y += 5

        elif (self.ball.pos_x < self.bumper_two.pos_x + self.bumper_two.width and
                    self.ball.pos_x + self.ball.size > self.bumper_two.pos_x and
                    self.ball.pos_y < self.bumper_two.pos_y + self.bumper_two.height and
                    self.ball.pos_y + self.ball.size > self.bumper_two.pos_y):
            self.ball.speed_x *= -1
            if self.bumper_two.moving_up:
                self.ball.speed_y -= 5
            elif self.bumper_two.moving_down:
                self.ball.speed_y += 5

    #Draw player scores on the screen
    def draw_score(self):
        p_one_score = self.score_font.render(str(self.player_one_points), True, self.red)
        p_two_score = self.score_font.render(str(self.player_two_points), True, self.red)
        self.game_display.blit(p_one_score, [self.screen_width / 4, self.screen_height / 6])
        self.game_display.blit(p_two_score, [(self.screen_width / 4)*3, self.screen_height / 6])

    #Draw everything in the screen
    def draw_screen(self):
        self.game_display.fill(self.black)
        self.draw_score()
        self.game_display.fill(self.white, rect=[self.bumper_one.pos_x, self.bumper_one.pos_y,
                                                 self.bumper_one.width, self.bumper_one.height])
        self.game_display.fill(self.white, rect=[self.bumper_two.pos_x, self.bumper_two.pos_y,
                                                 self.bumper_two.width, self.bumper_two.height])
        self.game_display.fill(self.white, rect=[self.ball.pos_x, self.ball.pos_y, self.ball.size, self.ball.size])
        self.game_display.fill(self.white, rect=[(self.screen_width / 2) - 1, 0, 2, self.screen_height])

    #Input handler for the single player game
    def handle_input_sp(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                # Keys for player one
                if event.key == pygame.K_s:
                    self.bumper_one.moving_down = True
                    self.bumper_one.moving_up = False

                if event.key == pygame.K_w:
                    self.bumper_one.moving_up = True
                    self.bumper_one.moving_down = False

                # Keys for player two
                if event.key == pygame.K_DOWN:
                    self.bumper_two.moving_down = True
                    self.bumper_two.moving_up = False

                if event.key == pygame.K_UP:
                    self.bumper_two.moving_up = True
                    self.bumper_two.moving_down = False

                # handle pause game
                if event.key == pygame.K_ESCAPE:
                    self.pause_game()

            if event.type == pygame.KEYUP:
                # keys for player one
                if event.key == pygame.K_s:
                    self.bumper_one.moving_down = False

                if event.key == pygame.K_w:
                    self.bumper_one.moving_up = False

                # keys for player two
                if event.key == pygame.K_DOWN:
                    self.bumper_two.moving_down = False

                if event.key == pygame.K_UP:
                    self.bumper_two.moving_up = False

        if self.bumper_one.moving_down:
            if self.bumper_one.pos_y < self.screen_height - self.bumper_one.height:
                self.bumper_one.move_down()

        if self.bumper_one.moving_up:
            if self.bumper_one.pos_y > 0:
                self.bumper_one.move_up()

        if self.bumper_two.moving_down:
            if self.bumper_two.pos_y < self.screen_height - self.bumper_two.height:
                self.bumper_two.move_down()

        if self.bumper_two.moving_up:
            if self.bumper_two.pos_y > 0:
                self.bumper_two.move_up()

    # handle pause situation
    def pause_game(self):
        paused = True
        pause_text = self.game_font.render("PAUSED", True, self.red)
        self.game_display.blit(pause_text, [self.screen_width / 2, self.screen_height / 2])
        pygame.display.update()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
            self.clock.tick(30)

    #exit game
    def exit_game(self):
        pygame.quit()
        quit()
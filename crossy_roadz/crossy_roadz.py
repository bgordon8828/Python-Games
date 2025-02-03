from ast import PyCF_ALLOW_TOP_LEVEL_AWAIT
import sys
from turtle import Screen
import pygame
from game_stats import GameStats
from button import Button
from settings import Settings
from froggy import Frog
from car import Car
from time import sleep
import random

class CrossyRoad:
    """Manages game assets and behaviors"""

    def __init__(self):
        """Initialize the game and create the game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Crossy Roadz")

        # Create an instance to store game stats #
        self.stats = GameStats(self)

        self.froggy = Frog(self)
        self.cars = pygame.sprite.Group()

        self._create_traffic()

        # Make the play button # 
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.froggy.update()
            self._update_objects()
            self._update_screen()
            self.froggy.moving_right = False
            self.froggy.moving_left = False
            self.froggy.moving_up = False
            self.froggy.moving_down = False

    def _create_traffic(self):
        """Create a group of cars"""
        # make a bunch of cars (we're talkin LA traffic) #
        h = self.settings.screen_height
        w = self.settings.screen_width
        n_cars = 8

        # create the first wave of cars #
        for i in range(n_cars):
            #create a car and put it in a new column
            car_obj = Car(self)
            car_obj.y = h*i/n_cars
            car_obj.rect.y = car_obj.y
            car_obj.update(i * random.randint(1,100)) #= self.settings.car_speed * i
            self.cars.add(car_obj)

        for j in range(n_cars):
            #create cars on the right moving to left
            car_obj2 = Car(self)
            car_obj2.y = int(h*(j+1)/n_cars)
            car_obj2.rect.y = car_obj2.y
            car_obj2.x = w
            car_obj2.rect.x = car_obj2.x
            car_obj2.update((-0.1*j))
            self.cars.add(car_obj2)

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset game stats #
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of remaining cars #
            self.cars.empty()

            #create new cars and center frog #
            self._create_traffic()
            self.froggy.center_frog()

            # hide the mouse cursor #
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.froggy.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.froggy.moving_left = False
        elif event.key == pygame.K_UP:
            self.froggy.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.froggy.moving_down = False
        if event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.froggy.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.froggy.moving_left = True
        elif event.key == pygame.K_UP:
            self.froggy.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.froggy.moving_down = True

    def _update_screen(self):
        """Update images on screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.froggy.blitme()
        h = self.settings.screen_height
        w = self.settings.screen_width
        for i in range(16):
            pygame.draw.lines(self.screen,pygame.Color(0,0,0),False,[(0,i*h/16),(w,i*h/16)])

        self.cars.draw(self.screen)

        # Draw the play button if the game is inactive #
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _update_objects(self):
        """Check to see if anything is at an edge, 
            then update the positions of it"""
        self._check_edges()
        self.froggy.update()
        self.cars.update(1)
        self._check_frog_top()


        # look for collisions # 
        if pygame.sprite.spritecollideany(self.froggy, self.cars):
            self._frog_hit()

    def _frog_hit(self):
        """Respond to frog being hit by an alien"""
        #Take away a frog #
        self.stats.frogs_left -= 1

        #get rid of cars #
        self.cars.empty()

        #create new cars and center the frog #
        self._create_traffic()
        self.froggy.center_frog()

        # Pause #
        sleep(0.5)

        

    def _check_edges(self):
        """Respond if anything reaches an edge"""
        if self.froggy.check_edges_x():
            self.froggy.rect.x += self.settings.frog_drop_speed
        if self.froggy.check_edges_y():
            self.froggy.rect.y += self.settings.frog_drop_speed
    
    def _change_direction(self):
        """Changes direction"""
    
    def _check_frog_top(self):
        """Check to see if the frog reached the top of the screen"""
        screen_rect = self.screen.get_rect()
        if self.froggy.rect.top <= screen_rect.top:
            # Treat as if it got hit by a car #
            self._frog_hit()

if __name__ == '__main__':
    # Make a game instance, and run the game #
    ai = CrossyRoad()
    ai.run_game()
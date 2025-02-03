import pygame
from pygame.sprite import Sprite

class Car(Sprite):
    """A class to represent a car in the game"""

    def __init__(self, ai_game):
        """Initialize the car and its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load in the car and set its rect attribute #
        self.images = pygame.image.load('images/car.bmp')
        h = self.settings.screen_height
        w = self.settings.screen_width
        self.image = pygame.transform.scale(self.images, (w/16,h/16))
        self.rect = self.image.get_rect()

        # start each car on the left side of screen #
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the car's exact horizontal position #
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if car is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self, inc):
        """Move the car to the right"""
        self.x += int(self.settings.car_speed * inc)
        self.rect.x = self.x
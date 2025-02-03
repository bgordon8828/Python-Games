import pygame


class Frog:
    """A class which defines the frog"""

    def __init__(self, ai_game):
        """Initializes the frog and its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the frog image and get its rect #
        self.images = pygame.image.load('images/frog.bmp')
        h = self.settings.screen_height
        w = self.settings.screen_width
        self.image = pygame.transform.scale(self.images, (w//16 - 4,h//16 - 4))
        self.rect = self.image.get_rect()

        # Start each frog at the bottom center of the screen #
        self.rect.midtop = (self.screen_rect.width//2, 15 * self.screen_rect.height // 16 + 2 )
        
        # Store a decimal value for the frog horizontal and vertical position #
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


        # Movement flag #
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def check_edges_x(self):
        """Return True if frog is at left or right edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def check_edges_y(self):
        """Return True if frog is at up or down edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """Update the ship's position based on the movement flag"""
        h = float(self.screen_rect.height) / 16
        w = self.rect.width
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += w #(self.settings.frog_speed * 
                            #self.settings.frog_direction)
        if self.moving_left and self.rect.left > 0:
            self.x -= w #(self.settings.frog_speed * 
                            #self.settings.frog_direction)
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= h #(self.settings.frog_speed * 
                            #self.settings.frog_direction)
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += h #(self.settings.frog_speed * 
                            #self.settings.frog_direction)
        
        # Update rect object from self.x. #
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_frog(self):
        """Center the frog on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
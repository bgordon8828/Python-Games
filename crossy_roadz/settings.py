class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings # 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # frog settings #
        self.frog_speed = 1.5
        self.frog_drop_speed = 10
        # 1 represents right; -1 represents left #
        self.frog_direction = 1
        self.frog_limit = 3

        # car settings # 
        self.car_speed = 1.5
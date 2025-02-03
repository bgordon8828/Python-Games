class GameStats:
    """Track stats for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # start in active state #
        self.game_active = False

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.frogs_left = self.settings.frog_limit
        
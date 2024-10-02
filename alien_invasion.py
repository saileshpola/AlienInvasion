import sys
import pygame

from GameFiles.settings import Settings
from GameFiles.ship import Ship


class AlienInvasion:
    "Class to manage game assets and behaviour."

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = self.settings.screen_bg_color
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.__check_events()
            self.__update_screen()
            self.clock.tick(60)

    def __update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.screen_bg_color)
        self.ship.draw_ship()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def __check_events(self):
        # Watch for keyboard and mouse events.
        for events in pygame.event.get():
            print(events)
            if events.type == pygame.QUIT:
                sys.exit()


pygame.quit()
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

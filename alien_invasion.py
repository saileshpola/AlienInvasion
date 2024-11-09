import sys
import pygame

from GameFiles.settings import Settings
from GameFiles.ship import Ship


class AlienInvasion:
    """Class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = self.settings.screen_bg_color
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.__check_events()
            self.__update_screen()
            self.ship.update_ship()
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
            elif events.type == pygame.KEYDOWN:
                self._check_keydown_events(events)
            elif events.type == pygame.KEYUP:
                self._check_keyup_events_(events)

    def _check_keyup_events_(self, events):
        if events.key == pygame.K_RIGHT:
            self.ship.ship_moving_right = False
        elif events.key == pygame.K_LEFT:
            self.ship.ship_moving_left = False

    def _check_keydown_events(self, events):
        if events.key == pygame.K_RIGHT:
            self.ship.ship_moving_right = True
        elif events.key == pygame.K_LEFT:
            self.ship.ship_moving_left = True
        elif events.key == pygame.K_q:
            sys.exit()


pygame.quit()
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

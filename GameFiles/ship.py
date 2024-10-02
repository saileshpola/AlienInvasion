import pygame.image


class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.ship_image = pygame.image.load("images/ship1.bmp")
        self.ship_image = pygame.transform.scale(self.ship_image, (100, 100))
        self.ship_rect = self.ship_image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.ship_rect.midbottom = self.screen_rect.midbottom

    def draw_ship(self):
        self.screen.blit(self.ship_image, self.ship_rect)

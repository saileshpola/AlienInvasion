import pygame.image


class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.ship_image = pygame.image.load("images/ship1.bmp")
        self.ship_image = pygame.transform.scale(self.ship_image, (75, 75))
        self.ship_rect = self.ship_image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.ship_rect.midbottom = self.screen_rect.midbottom

        # Store the ships x position as a float value
        self.x = float(self.ship_rect.x)

        self.ship_moving_right = False
        self.ship_moving_left = False

    def update_ship(self):
        if self.ship_moving_right and self.ship_rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.ship_moving_left and self.ship_rect.left > 0:
            self.x -= self.settings.ship_speed
        self.ship_rect.x = self.x

    def draw_ship(self):
        self.screen.blit(self.ship_image, self.ship_rect)

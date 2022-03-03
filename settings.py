#!/usr/bin/python3
import pygame.image


class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""
        # screen settings
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 2

        # bullet settings
        self.bullet_width = 3.0
        self.bullet_height = 15.0
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        # alien settings
        self.fleet_drop_speed = 10

        # how quickly the game speeds up
        self.speedup_scale = 1.2

        # how quicly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = 1.2
        self.bullet_speed = 5.0
        self.alien_speed = 0.5

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


def main():
    ...


if __name__ == '__main__':
    main()

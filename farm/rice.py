"""This module defines the Rice crop class."""

from farm.crop import Crop


class Rice(Crop):
    """Rice crop: gains 5 grains when watered, 10 when transplanted."""

    def water(self):
        """Add 5 grains to the rice crop."""
        self.grains += 5

    def transplant(self):
        """Add 10 grains to the rice crop."""
        self.grains += 10

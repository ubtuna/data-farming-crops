"""This module defines the Corn crop class."""

from farm.crop import Crop


class Corn(Crop):
    """Corn crop: gains 10 grains each time it is watered."""

    def water(self):
        """Add 10 grains to the corn crop."""
        self.grains += 10

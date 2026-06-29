"""This module defines the Crop parent class shared by all crops."""

# pylint: disable=too-few-public-methods


class Crop:
    """Parent class holding the shared behavior of all crops."""

    def __init__(self):
        self.grains = 0

    def ripe(self):
        """Return True when the crop has at least 15 grains."""
        return self.grains >= 15

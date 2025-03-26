"""
 Importing All Classes from a Module
"""

from class_modules import Car

class CarColor(Car):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    def describe_color(self):
        """Print a statement describing the battery size."""
        print(f"This car is {self.color.upper()}.")
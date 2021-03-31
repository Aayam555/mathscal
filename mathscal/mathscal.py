import math

class Pythagorus_Theorem():
    def hypotenuse(self, p, b):
        hypotenuse = math.sqrt((p**2 + b**2))
        return hypotenuse

    def base(self, p, h):
        base = math.sqrt((h**2 - p**2))
        return base

    def perpendicular(self, b, h):
        perpendicular = math.sqrt((h**2 - b**2))
        return perpendicular

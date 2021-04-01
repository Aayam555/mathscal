import math
import random

class Pythagorus_Theorem():
    def __init__(self, in_root=False):
        self.in_root = in_root

    def hypotenuse(self, p, b):
        hypotenuse_in_decimal = math.sqrt((p**2 + b**2))
        hypotenuse_in_root = p**2 + b**2

        if self.in_root:
            return hypotenuse_in_root

        else:
            return hypotenuse_in_decimal


    def base(self, p, h):
        base_in_decimal = math.sqrt((h**2 - p**2))
        base_in_root = h**2 - p**2

        if self.in_root:
            return base_in_root

        else:
            return base_in_decimal

    def perpendicular(self, h, b):
        perpendicular_in_decimal = math.sqrt((h**2 - b**2))
        perpendicular_in_root = h**2 - b**2

        if self.in_root:
            return perpendicular_in_root

        else:
            return perpendicular_in_decimal


def power(self, number, power):
    return number ** power
    
def distance_of_coordinates(self, coordinate1, coordinate2, in_root=False):
    x1 = coordinate1[0]
    y1 = coordinate1[1]
    x2 = coordinate2[0]
    y2 = coordinate2[1]

    distance_in_root = (x2-x1)**2 + (y2-y1)**2
    distance_in_decimal = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    if in_root:
        return distance_in_root

    else:
        return distance_in_decimal


def sum_of_interior_angles(self, number_of_sides):
    sum = (number_of_sides - 2) * 180
    return sum


def generate_random_numbers(self, min, max):
    number = random.randint(min, max)
    return number

class Temp_Scale_Converter():
    def c_to_f(self, c):
        f = ((c * 18)/10) + 32
        return f

    def f_to_c(self, f):
        c = (10 * (f-32)) / 18
        return c

    def f_to_k(self, f):
        k = ((10 * (f-32))/18) + 273
        return k

    def k_to_f(self, k):
        f = (18 * (k - 273))/10 + 32
        return f

    def k_to_c(self, k):
        c = k - 273
        return c

    def c_to_k(self, c):
        k = c + 273
        return k


def midpoint_of_coordinates(self, coordinate1, coordinate2, in_fraction=False):
    x1 = coordinate1[0]
    y1 = coordinate1[1]
    x2 = coordinate2[0]
    y2 = coordinate2[1]

    midpoint_in_decimal = (((x1 + x2)/2), ((y1 + y2)/2))
    midpoint_in_fraction = (str((x1 + x2)) + '/2', str((y1 + y2)) + '/2')
        
    if in_fraction:
        return midpoint_in_fraction

    else:
        return midpoint_in_decimal


def emi(self, p, r, n):
    r = r / 1200
    emi = (p * r * ((r+1)**n))/(((1+r)**n) - 1)
    return emi


def slope_of_coordinates(self, coordinate1, coordinate2, in_fraction=False):
    x1 = coordinate1[0]
    y1 = coordinate1[1]
    x2 = coordinate2[0]
    y2 = coordinate2[1]

    slope_in_decimal = (y2 - y1)/(x2 - x1)
    slope_in_fraction = str((y2 - y1)) + '/' + str((x2-x1))
        
    if in_fraction:
        return slope_in_fraction

    else:
        return slope_in_decimal


def multiplication_table_generator(self, number, end):
    for i in range(1, end+1):
        print(number, '*', i, '=', number*i)


def check_prime(self, number):
    prime = True
    if number % 2 == 0 and number != 2:
        prime = False

    elif number == 2:
        prime = True

    else:
        for i in range(2, number):
            if number % i == 0:
                prime = False
            
    return prime

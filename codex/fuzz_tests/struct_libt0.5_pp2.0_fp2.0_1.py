import _struct
import math
from math import *
import random
import operator
import time

def generate_random_points(n):
    return [random.uniform(-1, 1) for _ in range(n)]

def generate_random_points_around(n, points, radius):
    return [random.uniform(p - radius, p + radius) for p in points]

def generate_random_points_around_gaussian(n, points, radius):
    return [random.gauss(p, radius) for p in points]

def generate_random_points_around_gaussian_with_bounds(n, points, radius, min_bound, max_bound):
    points = [random.gauss(p, radius) for p in points]
    points = [max(min(p, max_bound), min_bound) for p in points]
    return points

def generate_random_points_around_gaussian_with_bounds_and_random_radius(n, points, radius, min_bound, max_bound):
    points = [random.gauss(p

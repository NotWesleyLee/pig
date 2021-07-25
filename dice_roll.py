""" Program to generate a random die roll"""

import random

def roll(seed=None):
    """Generate a random number"""
    random.seed(seed)
    return random.randint(1, 6)

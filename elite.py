#!/usr/bin/env python3

"""
Wrapper script for `pyplanets.py`.

Laszlo Szathmary (jabba.laci@gmail.com)
"""

import random
from random import randint

import pyplanets

galaxy = pyplanets.Galaxy()


def get_random_planet_from_galaxy1():
    """
    Get a planet's name from Galaxy 1.
    """
    galaxy.goto_galaxy(1)
    return random.choice(galaxy.planets)


def get_random_planet_from_galaxy(num):
    """
    Get a planet's name from Galaxy X, where
    X is between 1 and 8.
    """
    assert 1 <= num <= 8
    #
    galaxy.goto_galaxy(num)
    return random.choice(galaxy.planets)


def get_random_planet():
    """
    Get a planet's name from the available 8 galaxies.
    """
    num = randint(1, 8)
    return get_random_planet_from_galaxy(num)


def main():
    """
    Print planet names in the current galaxy.
    """
    print(galaxy.planets)

#############################################################################

if __name__ == "__main__":
    # main()
    print(get_random_planet_from_galaxy1())
    print(get_random_planet_from_galaxy(2))
    print(get_random_planet())

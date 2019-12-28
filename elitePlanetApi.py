#!/usr/bin/env python3

import random

import pyplanets
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/planet")
def getPlanet():
    galaxy = pyplanets.Galaxy()
    galaxy.goto_galaxy(1)
    #
    return random.choice(galaxy.planets)

if __name__ == "__main__":
    app.run()

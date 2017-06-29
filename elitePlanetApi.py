from flask import Flask
import pyplanets
import random

app = Flask(__name__)

@app.route("/planet")
def getPlanet():

    galaxy = pyplanets.Galaxy()
    galaxy.goto_galaxy(1)

    return random.choice(galaxy.planets)

if __name__ == "__main__":
    app.run()

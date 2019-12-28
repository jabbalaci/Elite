#!/usr/bin/env python3

"""
I found the original pytxtelite at
http://automaticromantic.com/static/misc/pytxtelite.txt .
pytxtelite is a conversion of Ian Bell's txtelite.c 1.2 (and parts of 1.4)
to python (2.5, maybe earlier).

As I was interested in planet names only, I removed everything
else. This script contains the minimum for generating planet
names.

It also has a simple command-line interface for printing planet names (n)
and for jumping to the next galaxy (j).

I made a simple wrapper script too called elite.py. If you want to get
the name of a random planet, use elite.py.

Laszlo Szathmary (jabba.laci@gmail.com)
"""

import cmd

pairs0  = "ABOUSEITILETSTONLONUTHNO"
pairs = "..LEXEGEZACEBISOUSESARMAINDIREA.ERATENBERALAVETIEDORQUANTEISRION"
pairs1 = pairs0 + pairs


def size16Num(value):
    """Keep a number within 16 bits, Miki Tebeka, comp.lang.python post"""
    mask = (1 << 16) - 1
    return value & mask


def rotate1(x):
    """Rotate 8 bit number leftwards"""
    temp = x & 128
    return (2 * (x & 127)) + (temp >> 7)


def twist(x):
    return (256 * rotate1(x >> 8)) + rotate1(x & 255)


##########
## Seed ##
##########

class Seed:
    """A pseudo-random number holder based on 16 bit numbers."""
    def __init__(self):
        self.w0 = 0
        self.w1 = 0
        self.w2 = 0

    def shuffle(self):
        """Pseudo Randomize a seed"""
        temp = size16Num(self.w0 + self.w1 + self.w2)
        self.w0 = self.w1
        self.w1 = self.w2
        self.w2 = temp


############
## Galaxy ##
############

class Galaxy:
    def __init__(self):
        """A galaxy.

           In the original game all system data was generated from the initial
           seed value for galaxy one. If you want a later galaxy you have to
           advance through to get it.
        """
        self.planets = []
        self.seed = Seed()
        self.setGalaxyOne()
        self.makeSystems()

    def makeSystems(self):
        """Populate all the planets"""
        self.planets = []

        #Populate the 256 planetary planets in each galaxy
        for _ in range(256):
            self.planets.append(self.makeplanet())

    def goto_galaxy(self, galnum):
        """Goto galaxy X, where 1 <= X <= 8
        Galaxy 9 == Galaxy 1"""
        self.setGalaxyOne()

        #Advance to further galaxies if need-be.
        for _ in range(2, galnum + 1):
            self.nextgalaxy()

        self.galaxy_number = galnum % 8
        self.makeSystems()

    def setGalaxyOne(self):
        """Set base seed for galaxy 1"""
        self.seed.w0 = 0x5A4A
        self.seed.w1 = 0x0248
        self.seed.w2 = 0xB753
        self.galaxy_number = 1

    def nextgalaxy(self, make_planets=True):
        """Apply to galaxy1 seed once for galaxy 2, twice for galaxy 3 etc
           Eighth application gives galaxy 1 again"""
        ss = self.seed
        ss.w0 = twist(ss.w0)
        ss.w1 = twist(ss.w1)
        ss.w2 = twist(ss.w2)

    def makeplanet(self):
        """Make a planetary system"""
        s = self.seed

        longnameflag = s.w0 & 64

        pair1=2*(((s.w2)>>8)&31)
        s.shuffle()
        pair2=2*(((s.w2)>>8)&31)
        s.shuffle()

        pair3=2*(((s.w2)>>8)&31)
        s.shuffle()


        pair4=2*(((s.w2)>>8)&31)
        s.shuffle()

        # Always four iterations of random number
        name = []
        name.append(pairs[pair1])
        name.append(pairs[pair1+1])
        name.append(pairs[pair2])
        name.append(pairs[pair2+1])
        name.append(pairs[pair3])
        name.append(pairs[pair3+1])

        if longnameflag: #* bit 6 of ORIGINAL w0 flags a four-pair name
            name.append(pairs[pair4])
            name.append(pairs[pair4+1])
        planet_name = "".join(name).replace('.','')
        # capitalize
        planet_name = planet_name.capitalize()
        return planet_name

    def planet_names(self):
        for planet in self.planets:
            print(planet)

    def nextGalaxy(self):
        """Galactic hyperspace to next galaxy"""
        self.goto_galaxy(self.galaxy_number+1)


####################
## TradingGameCmd ##
####################

class TradingGameCmd(cmd.Cmd):
    """Command interface to a TradingGame"""

    def __init__(self):
        self.galaxy = Galaxy()
        cmd.Cmd.__init__(self)
        self.setPrompt()

    def setPrompt(self):
        self.prompt = '> '

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_j(self, line):
        """galhyp - Use galactic hyperdrive to jump to the next galaxy"""
        self.galaxy.nextGalaxy()
        print("You appear in galaxy {g}".format(g=self.galaxy.galaxy_number))

    def do_n(self, line):
        self.galaxy.planet_names()

    def do_q(self, line):
        """Quit the game"""
        print("Goodbye!")
        return True

    def do_EOF(self, line):
        print()
        return True

    def do_intro(self,line):
        """Show introduction"""
        print('\n'.join(["",
                         "n    (planet names)\n"
                         "j    (jumps to next galaxy)\n",
                        ]))

#############################################################################

if __name__ == "__main__":
    tg = TradingGameCmd()
    tg.do_intro('')
    tg.cmdloop()

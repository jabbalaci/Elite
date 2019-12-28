Elite Planet Name Generator
===========================

I found the original pytxtelite (written by Ian Sparks) at
<http://automaticromantic.com/static/misc/pytxtelite.txt>.
You can find a copy of the original script in the "pytxtelite" folder.

pytxtelite is a conversion of Ian Bell's txtelite.c 1.2 (and parts of 1.4)
to Python (2.5, maybe earlier).

As I was interested in planet names only, I removed everything
else. This script contains the minimum for generating planet
names.

It also has a simple command-line interface for printing planet names (n)
and for jumping to the next galaxy (j).

I made a simple wrapper script too called `elite.py`. If you want to get
the name of a random planet, use `elite.py`.

Examples
--------

Print the planet names in Galaxy 1:

    import pyplanets

    galaxy = pyplanets.Galaxy()
    print(galaxy.planets)

Print the name of a random planet:

    import random
    ...
    print(random.choice(galaxy.planets))

Author
------

* Laszlo Szathmary (<jabba.laci@gmail.com>)
* Homepage: <http://pythonadventures.wordpress.com/2012/03/06/elite-planet-name-generator/>

Rest API
--------

This part was added by Richard Hannah (<richard.hannah1974@gmail.com>).

    python elitePlanetApi.py

Then navigate to <http://localhost:5000/planet>.

Links
-----

* Ian Bell's Text Elite Page (<http://www.iancgbell.clara.net/elite/text/index.htm>): A C implementation of the classic Elite trading system.
* [richcarl/txtelite](https://github.com/richcarl/txtelite): An Erlang version of Ian Bell's "text Elite". Also contains an updated version of the original C code.

import gc, weakref

import numpy as np

from pylab import *

import jcoords, transforms

# local imports
import config, utils

# weakrefs to avoid circular refs
_jcoords = weakref.ref(jcoords)
_transforms = weakref.ref(transforms)

class KeplerSystem(object):
    """ A system of keplerian orbits.
    """

    def __init__(self, *args, **kw):
        """ Initialize the system.
        """
        # set up the standard list of options
        self.options = Options(
            a=0.0,
            e=0.0,
            i=0.0,
            Om=0.0,
            om=0.0,
            M=0.0,
            T=0.0,
            P=0.0,
            **kw
        )

        # a list of orbital elements
        # in this case, a list of tuples
        self.orbs = []

        # add orbits supplied in args
        self.add_orbits(*

import types
types.ModuleType.__repr__ = lambda self: '<module %r>' % self.__name__

# This is the standard library
import sys
import os
import time
import math
import random
import copy

# Import some of the modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Import the modules from the other files
import constants
import functions
import classes

# Run the main function
if __name__ == "__main__":
    functions.main()

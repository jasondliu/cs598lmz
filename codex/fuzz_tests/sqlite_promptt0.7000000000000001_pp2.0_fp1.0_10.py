import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')

import matplotlib.pyplot as plt
import numpy as np


# -*- coding: utf-8 -*-

"""
The :mod:`pynbody.plot` module provides functions for making a variety of plots
of simulation data.

To use it, type:

>>> import pynbody.plot as pp

The :mod:`pynbody.plot` module also provides a simple framework for making
custom plots. To make a new plot, simply subclass
:class:`pynbody.analysis.GenericPlot` and implement the ``_calculate`` method.
You can then override the ``_plot`` method if your plot needs to do anything
special with the data; otherwise, the default implementation will use Matplotlib
to generate publication-quality plots.

The following is an example of a simple histogram plot which calculates the
relative masses of the different particle types in the simulation.

>>> import pynbody.plot as pp
>>> import pynbody.analysis as pa
>>> import numpy as np
>>> class ParticleHistogram(

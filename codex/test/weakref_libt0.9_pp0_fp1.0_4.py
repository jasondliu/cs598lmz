import weakref
from types import MethodType

from cycler import Cycler
from copy import deepcopy
from pylab import *  # imports module `matplotlib.pylab`, too
from pylab import rcParams
import matplotlib.pyplot as plt
import numpy as np

from ..plotting import do_plot
from ._default import Default
from .load import load
from .param import register_param
from .storage import register_storage, get_storage
from .util import next_tuple, uid

_marker_ids = itertools.count()


@register_param
class _PlotBase(Default):
    """Base class of all plotters."""

    # To make sure that the description is not stored in the global store
    description = ""
    _description = ""

    def __init__(self):
        # the item is the id of this instance
        # it needs to be unique within its class
        self.id = uid(type(self))
        self.kwargs = {}

    # --------------------------------------------------------------------------
    # Methods to do plotting
    #



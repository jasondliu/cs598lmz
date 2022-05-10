import weakref

import numpy as np

from ..items import Table  # , Column
from ..core.util.misc import load_wine
from ..core.neutronprops import hydrogen_sld
from ..core.qrange import q_projection, qrange
from .geometries import Geometry, Parameter
from .sources import Source
from .kernel import Kernel
from .optimize import Optimizer
from .invariant import Invariant
from .priors import Theory
from ..core.workspace import get_qspace
from ..core.edges import EdgeFactory
from ..core.function import Function
from ..core.pdf import PDF
from ..core.fitter import DefaultFitter
from ..core.models import Model
from ..core.config import config, reset_config


class Component(object):
    """
    Holds a set of parameters and a set of geometries.

    Parameters
    ----------
    name : str
        The name of the component.
    category : {"source", "detector", "sample"}
        The category is used to place the component in the hierarchy of models.

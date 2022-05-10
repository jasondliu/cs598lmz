import weakref
from time import time

from numpy import pi, inf, array

from .components import Component
from .utilities import indent, indent_if
from .utilities.exceptions import *
from .utilities.decorators import lazy_property, lazy_attribute
from .utilities.iteration import deep_iter
from .utilities.warnings import DeprecationWarning


class System(object):
    """
    A System is a collection of Components that can be used to build a
    network.  A System may be a SubSystem of another System.  All
    Components must be contained in a System.

    Attributes
    ----------
    name : str
        The name of the System.
    subsystems : list of Systems
        The Systems contained within this System.
    components : list of Components
        The Components contained within this System.
    ports : list of Ports
        Ports contained within this System.
    connections : list of Connections
        Connections contained within this System.
    subsystems_and_components : list of Systems and Components
        The Systems and Components contained within this System.
    subsystem

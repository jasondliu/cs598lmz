import select
from collections import defaultdict
from math import floor

from numpy.random import random_sample, choice

from enum import Enum
from palettable.colorbrewer.sequential import Purple_9

from simpy import Resource, Store, Environment, Process
from simpy.resources.resource import BaseCapacity
from simpy.resources.resource import ResourceWrapper
from simpy.resources.store import FilterStore
from simpy.events import Timeout
from simpy.util import start_delayed
from simpy.core import BoundClass

from logging import debug
from . import util
from . import agents
from . import factories
from . import markup
from . import layout
from . import view
from . import world


class Product(object):
    def __init__(self, guid, name):
        self.guid = guid
        self.name = name


class Alteration(Enum):
    DELAY = 1
    CORRECTION = 2


class AlterationSubType(Enum):
    MINOR_PRODUCT_ERROR = 1
    MAJOR_PRODUCT_ERROR =

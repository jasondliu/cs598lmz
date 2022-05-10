import gc, weakref, abc, os, logging, math
import numpy as np
import numpy.random as npr
from typing import List, Callable, Any, Type, Optional, Tuple, Sequence, Union, Generator, Set, TypeVar, Hashable
from collections import OrderedDict
from collections.abc import Container
from functools import partial
from copy import copy
from multiprocessing import Process, Pipe, Queue
from multiprocessing.connection import Connection
from threading import Thread
from copy import copy
from queue import Full
import traceback
import pickle
from enum import Enum
from sortedcollections import SortedDict
import sys
import pickle
from types import CodeType

from . import environments
from . import keygeneration as keyg
from . import results
from .results import EpisodeResults
from . import utils

_main_process_id = os.getpid()

class StateType(Enum):
    """An enumeration indicating the type of state used by an environment."""
    DISCRETE = 1
    CONTINUOUS = 2
    MIXED = 3

def

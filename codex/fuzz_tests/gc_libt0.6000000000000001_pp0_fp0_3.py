import gc, weakref
from collections import defaultdict
from itertools import count

import numpy

from theano.compile import optdb
from theano.compile.mode import Mode
from theano.gof import utils
from theano.gof.python25 import all, any, maxsize
from theano.gof.python25 import OrderedDict
from theano.gof.toolbox import KeyedList
from theano.gof.utils import flatten
from theano import config

from theano.printing import Print
from theano.printing import debugprint
from theano.misc.ordered_set import OrderedSet

from theano import gof

# This is imported here to avoid a circular import.
from theano.compile import profiling

_logger = logging.getLogger("theano.compile.function_module")

# If a Function object has a .maker attribute, it will be used to make a
# FunctionMaker object that will be used to make an OpFromGraph instance.
# The function will be called with the following arguments:
#     inputs: a

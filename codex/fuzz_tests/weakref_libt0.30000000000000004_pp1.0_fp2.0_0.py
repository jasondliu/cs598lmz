import weakref

import numpy as np

from . import _pywrap
from . import _pywrap_utils
from . import _pywrap_tensor
from . import _pywrap_variable
from . import _pywrap_variable_store
from . import core
from . import framework
from . import autograd
from . import function
from . import io
from . import layers
from . import optimizer
from . import parallel
from . import profiler
from . import variable

from .core import *
from .framework import *
from .autograd import *
from .function import *
from .io import *
from .layers import *
from .optimizer import *
from .parallel import *
from .profiler import *
from .variable import *

from . import contrib

from .contrib import *

from . import compat as _compat

from . import data_loader
from . import layers
from . import loss
from . import metrics
from . import nn
from . import optim
from . import utils

from .data_loader import *
from .layers import

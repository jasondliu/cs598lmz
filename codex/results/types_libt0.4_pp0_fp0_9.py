import types
types.ModuleType.__dict__['__getattr__'] = lambda self, name: types.ModuleType(self.__name__ + '.' + name)

from . import __version__
from . import __author__
from . import __license__
from . import __url__
from . import __doc__

from . import core
from . import utils
from . import data
from . import io
from . import viz
from . import models
from . import stats
from . import simulate
from . import plot
from . import animate
from . import tests
from . import examples
from . import notebooks

from .core import *
from .utils import *
from .data import *
from .io import *
from .viz import *
from .models import *
from .stats import *
from .simulate import *
from .plot import *
from .animate import *
from .tests import *
from .examples import *
from .notebooks import *

from . import util
from .util import *

# Import all submodules
from . import *

# Cleanup namespace
del types, util

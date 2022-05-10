import types
types.ModuleType.__repr__ = module_repr

# Add a special formatting for numpy arrays
def array_str(a): return "np."+a.__str__()
np.ndarray.__str__ = array_str

# Make import * work properly
for m in [np, scipy, pylab]:
    __all__ += m.__all__

# Suppress flow control warnings in Theano
warnings.filterwarnings('ignore', '.*theano.*')

from . import config
from .config import *

# Import most common subpackages
from . import arrays
from . import functions
from . import images
from . import io
from . import misc
from . import models
from . import plot
from . import stats

# Import most common objects into main namespace
from .arrays import *
from .functions import *
from .images import *
from .io import *
from .misc import *
from .models import *
from .plot import *
from .stats import *

# Import test runner
from . import testing
from .testing import run_tests

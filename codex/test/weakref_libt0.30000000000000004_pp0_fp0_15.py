import weakref

import numpy as np
import pandas as pd

from . import config
from . import core
from . import utils
from . import plotting
from . import io
from . import preprocessing
from . import stats
from . import models
from . import backend
from . import frontend
from . import _version

__version__ = _version.get_versions()['version']
del _version

# Set the default backend
backend.set_backend(config.default_backend)

# Set the default plotting backend
plotting.set_backend(config.default_plotting_backend)

# Set the default logging level
logging.basicConfig(level=config.default_log_level)

# Register the default logging handler
logger = logging.getLogger('pymc3')
logger.addHandler(logging.NullHandler())

# Set the default float type
theano.config.floatX = config.default_float

# Set the default numpy random generator
np.random.seed(config.default_seed)

# Set the

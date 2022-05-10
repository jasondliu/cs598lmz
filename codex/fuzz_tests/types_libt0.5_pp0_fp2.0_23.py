import types
types.ModuleType = types.ModuleType

# Import submodules
from . import data
from . import models
from . import utils

# Import the main API
from .api import *

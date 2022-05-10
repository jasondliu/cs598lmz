from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda x: x

from fbs import path, FB_PYTHON_37_OR_HIGHER
from fbs._context import _context
from fbs._context_util import get_context, set_context
from fbs_runtime import platform
from fbs_runtime.application_context import ApplicationContext
from fbs_runtime.exceptions import FbsError

from . import resources as _resources
from .application_context import cached_property
from .application_context import get_resource
from .application_context import get_resource_path
from .application_context import get_resource_paths
from .application_context import get_resource_string
from .application_context import prepare_resources
from .application_context import set_logging_level
from .application_context import set_resource_path
from .application_context import set_resource_paths
from .cmdline import main
from .constants import APP_NAME
from .constants import AUTHOR
from .constants import COPYRIGHT
from .constants import DEVELOPER
from .constants import MAIN
from .constants

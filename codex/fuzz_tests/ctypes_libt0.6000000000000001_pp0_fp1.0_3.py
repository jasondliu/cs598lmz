import ctypes
ctypes.cdll.LoadLibrary("libc.so.6")
libc = ctypes.CDLL("libc.so.6")

from . import cli
from . import config
from . import debug
from . import edition
from . import errors
from . import formats
from . import helpers
from . import linter
from . import logging
from . import minifier
from . import mtimes
from . import options
from . import parse
from . import plugins
from . import reporter
from . import resources
from . import shell
from . import stylesheet
from . import util
from . import version


_log = logging.getLogger(__name__)


# -----------------------------------------------------------------------------
# Public API
# -----------------------------------------------------------------------------
def check(paths,
          checkpoints=None,
          format=None,
          ignore=None,
          include=None,
          ignore_lint=None,
          ignore_lint_exceptions=None,
          ignore_no_checkpoint=False,
          ignore_no_files=False,
          ignore_warnings=False,
          include_lint=None,

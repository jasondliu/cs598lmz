import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import __version__


# Local imports
from . import util, command, model, settings
from .util import get_path_for_import, UserError, CommandError
from .util import ProgressDisplay, ProgressCounter, ProgressIndicator
from .command import Command, CommandContainer
from .model import Model, ModelContainer
from .settings import Settings
from .registry import get_registry, get_component, set_default_component
from .file_locks import GlobalFileLock, MultiFileLock, NoLock, FileLock
from .exceptions import ConfigurationError


# Logging
# ~~~~~~~

import logging
logger = logging.getLogger('datalad.interface')


# Entry point
# ~~~~~~~~~~~


def main(args=None):
    """Entry point

    Parameters
    ----------
    args : list of str, optional
      Arguments to process. If not provided, ``sys.argv[1:]`` is used.

    Notes
    -----
    If a ``ValueError`` is raised during processing, the error message

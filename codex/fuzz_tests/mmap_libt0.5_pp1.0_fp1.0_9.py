import mmap
import os
import re
import subprocess
import sys
import tempfile

from . import constants
from . import errors
from . import utils
from . import vfs
from . import vfs_metadata
from . import vfs_plugin
from . import vfs_registry

from .data_store import errors as data_store_errors
from .data_store import sqlite_file

from .frontend import log_utils

from .lib import definitions
from .lib import errors as lib_errors
from .lib import utils as lib_utils

from .objects import collector
from .objects import file_system
from .objects import file_system_searcher
from .objects import file_system_searcher_mediator
from .objects import file_system_searcher_queue
from .objects import path_spec
from .objects import serializer


class StorageFile(file_system.File):
  """Class that implements a storage file."""

  def __init__(
      self, resolver_context, file_system, path_spec, is_root=False,
     

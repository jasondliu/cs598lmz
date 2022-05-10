import mmap
import os
import re
import sys
import time
from collections import namedtuple
from datetime import datetime

from . import __version__
from . import config
from . import constants
from . import errors
from . import utils
from . import vcs
from . import version
from . import wheel
from .constants import PIP_DELETE_MARKER_FILENAME
from .exceptions import CommandError, PreviousBuildDirError
from .utils.deprecation import deprecated
from .utils.hashes import Hashes
from .utils.logging import indent_log
from .utils.misc import (
    display_path, dist_is_local, dist_in_usersite, dist_is_editable,
    dist_is_installable, egg_link_path, ensure_dir, get_installed_version,
    normalize_path, path_to_display, redact_auth_from_url,
    rmtree, unpack_file_url_to_path,
)
from .utils.packaging import get_metadata, get_pkg_info_revision

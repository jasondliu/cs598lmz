import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, fd, 0)

import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from collections import OrderedDict

from . import compat
from . import constants
from . import errors
from . import util
from . import vcs
from .compat import (
    PY2,
    IS_WINDOWS,
    text_type,
    string_types,
    iteritems,
    itervalues,
)
from .util import (
    display_path,
    rmtree,
    make_executable,
    make_vcs_requirement_url,
    normalize_path,
    splitext,
    unzip_file,
    rmtree,
    call_subprocess,
    format_size,
    create_tracked_tempdir,
    path_to_url,
)
from .vcs import vcs_supported
from .vcs import VcsSupport
from .vcs import NoSv

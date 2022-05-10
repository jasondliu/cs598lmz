import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

from . import config
from . import util
from . import version

# TODO: This is a hack to get around the fact that the default
#       python-apt version in Ubuntu 12.04 is too old.
#       Remove this when we drop support for 12.04.
try:
    import apt_pkg
except ImportError:
    sys.path.insert(0, '/usr/lib/python2.7/dist-packages')
    import apt_pkg

apt_pkg.init()

# TODO: This is a hack to get around the fact that the default
#       python-apt version in Ubuntu 12.04 is too old.
#       Remove this when we drop support for 12.04.
try:
    from apt.cache import Cache
except ImportError:
    from apt_pkg import Cache

from . import logger

log = logger.getLogger(__name__)

# TODO: This is a hack to get around the fact that the default
#       python-

import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib
import zipfile

from distutils.version import LooseVersion

from . import config
from . import constants
from . import errors
from . import log
from . import util
from . import version

# TODO(crbug.com/1055447): Remove this once the issue is fixed.
# Workaround for https://bugs.python.org/issue37373.
sys.modules['_frozen_importlib'] = None
sys.modules['_frozen_importlib_external'] = None

# TODO(crbug.com/1055447): Remove this once the issue is fixed.
# Workaround for https://bugs.python.org/issue37373.
sys.modules['_frozen_importlib'] = None
sys.modules['_frozen_importlib_external'] = None

# TODO(crbug.com/1055447): Remove this once the issue is fixed.
# Workaround for https://bugs.python.org/

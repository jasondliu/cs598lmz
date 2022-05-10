import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

from distutils.version import LooseVersion

from . import config
from . import constants
from . import errors
from . import log
from . import util
from . import version

# pylint: disable=too-many-lines

# The default location of the Android SDK.
DEFAULT_SDK_ROOT = os.path.join(os.path.expanduser('~'), 'Library', 'Android', 'sdk')

# The default location of the Android NDK.
DEFAULT_NDK_ROOT = os.path.join(os.path.expanduser('~'), 'Library', 'Android', 'sdk', 'ndk-bundle')

# The default location of the Android NDK.
DEFAULT_NDK_ROOT_LINUX = os.path.join(os.path.expanduser('~'), 'Android', 'Sdk', 'ndk-bundle')

# The default location of the Android NDK.
DE

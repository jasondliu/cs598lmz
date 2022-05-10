import mmap
import os
import re
import sys

from tempfile import NamedTemporaryFile
from typing import Dict, Iterable, List, Tuple, cast

from camisole.languages.c import build_command as _build_command
from camisole.models import Lang
from camisole.utils import CMakeVar


# When calling the CMakeLists.txt file, this environment variable is set to
# the install directory, so we can find SWOFT binaries in
# bin/Release/swoft.exe / bin/x64/Release/swoft.exe.
SWOFT_INSTALL_DIR = CMakeVar('SWOFT_INSTALL_DIR')

# Also set the install path in the environment, so it can be found in the
# compile command.
SWOFT_INSTALL = (
    '{es‌​cape}\\"${{SWOFT_INSTALL}}${{SWOFT_USE_MINGW}}\\"')

# Sticky global variables for SWOFT.
SWOFT_USE_MINGW = CMakeVar('SWOFT

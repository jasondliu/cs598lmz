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
from . import vcs

# This is the default version of the build script.
# It is used when the user does not specify a version.
DEFAULT_VERSION = '3.0'

# This is the version of the build script that is used by the
# buildbots.
BUILDBOT_VERSION = '3.0'

# This is the version of the build script that is used by the
# buildbots.
BUILDBOT_VERSION = '3.0'

# The default build script version to use.
DEFAULT_BUILD_SCRIPT_VERSION = DEFAULT_VERSION

# The default build script version to use for the buildbots.
BUILDBOT_BUILD_SCRIPT_VERSION = BUILDBOT_VERSION

# The default build script version to use for the buildbots.
BUILDBOT_BUILD_SCRIPT_VERSION = BUILDBOT_VERSION

# The default build script version to use for

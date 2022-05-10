import mmap
import os
import re
import subprocess
import sys
import tempfile
import time

from . import config
from . import constants
from . import errors
from . import utils
from . import vcs
from . import version

# TODO(david): Remove this once we have a better way to detect whether we're
# running in a buildbot.
_BUILDBOT_PATTERN = re.compile(r'^build\d+-m\d+$')

# TODO(david): Remove this once we have a better way to detect whether we're
# running in a buildbot.
_BUILDBOT_USER = 'chrome-bot'

# TODO(david): Remove this once we have a better way to detect whether we're
# running in a buildbot.
_BUILDBOT_HOST = 'build.chromium.org'

# TODO(david): Remove this once we have a better way to detect whether we're
# running in a buildbot.
_BUILDBOT_HOST_PATTERN = re.compile(r

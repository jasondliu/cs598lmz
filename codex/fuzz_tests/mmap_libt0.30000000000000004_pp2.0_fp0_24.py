import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback

import jinja2

from . import config
from . import util
from . import version
from . import xcode
from . import xcode_util
from . import xcrun
from . import xctest
from . import xctest_util
from . import xcuitest
from . import xcuitest_util

from . import build_util
from . import ios_util
from . import xctest_runner

from .build_util import BuildError
from .ios_util import IOS_SDK_VERSION_REGEX
from .xctest_runner import XCTestRunner

logger = logging.getLogger(__name__)

# The name of the generated xcode project.
PROJECT_NAME = 'Flutter'

# The name of the generated xcode workspace.
WORKSPACE_NAME = 'Flutter'

# The name of the generated xcode scheme.
SCHEME_NAME = 'Runner'


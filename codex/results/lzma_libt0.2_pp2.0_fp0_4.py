import lzma
lzma.LZMAFile

import sys
import os
import re
import shutil
import subprocess
import tempfile
import time
import urllib.request
import urllib.parse
import urllib.error
import zipfile

from distutils.version import LooseVersion

from . import utils
from . import version

# The default location of the SDK.
DEFAULT_SDK_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'sdk')

# The default location of the SDK.
DEFAULT_SDK_URL = 'https://github.com/flutter/flutter/releases/download/' \
                  'v{version}/flutter_macos_v{version}-stable.zip'

# The default location of the engine.
DEFAULT_ENGINE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'engine')

# The default location of the engine.
DEFAULT_ENGINE_URL = 'https://storage

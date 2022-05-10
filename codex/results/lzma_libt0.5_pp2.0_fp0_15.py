import lzma
lzma.LZMAError

import argparse
import sys
import os
import shutil
import subprocess
import stat
import time
import glob
import re
import pkg_resources
import json
import platform
import warnings
import tarfile
import zipfile
import io

from collections import OrderedDict

from distutils.spawn import find_executable
from distutils.version import LooseVersion

from jinja2 import Environment, FileSystemLoader

from . import __version__
from . import __version_info__
from . import __title__
from . import __description__
from . import __url__
from . import __author__
from . import __author_email__
from . import __license__
from . import __copyright__
from . import __python_requires__
from . import __classifiers__
from . import __keywords__
from . import __project_urls__
from . import __platforms__
from . import __supported_python_versions__
from . import __supported_platforms__
from . import __supported_architectures__
from . import

import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import zipfile

from distutils.version import LooseVersion
from xml.etree import ElementTree

import build_utils
import build_utils.config as config
import build_utils.version as version

# TODO:
# - Add support for building with VS2013.
# - Add support for building with VS2015.
# - Add support for building with VS2017.
# - Add support for building with VS2019.
# - Add support for building with VS2010.
# - Add support for building with VS2012.
# - Add support for building with VS2008.
# - Add support for building with VS2005.
# - Add support for building with VS2003.
# - Add support for building with VS2002.
# - Add support for building with VS6.
# - Add support for building with VS5.
# - Add support for building with VS4.
# - Add support for building with VS3.
# - Add support for building with VS2.
# - Add support for building with

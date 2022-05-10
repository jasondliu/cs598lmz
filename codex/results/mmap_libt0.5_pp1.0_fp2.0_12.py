import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib2

from base import *
from base import _
from base import _f
from base import _p
from base import _u
from base import _v
from base import _v3
from base import _v4
from base import _z
from base import _z3
from base import _z4
from base import __version__
from base import __version_info__
from base import PY2

# The list of files to be excluded from the source distribution.
EXCLUDE_FILES = [
    '*~',
    '*.bak',
    '*.bat',
    '*.bin',
    '*.cmd',
    '*.com',
    '*.db',
    '*.dll',
    '*.exe',
    '*.exp',
    '*.ilk',
    '*.lib',
    '*.log',
    '*.obj',
    '*.pdb',
    '*.pyc',
    '*.pyo',
   

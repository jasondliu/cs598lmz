import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

from contextlib import contextmanager
from distutils.version import LooseVersion
from functools import partial
from itertools import chain


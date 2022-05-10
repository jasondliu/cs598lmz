import lzma
lzma.LZMAFile

import os
import sys
import time
import shutil
import subprocess
import tempfile
import threading
import traceback

import pytest

from . import util
from . import test_util
from . import test_support
from . import test_zipfile
from . import test_tarfile
from . import test_lzma
from . import test_bz2
from . import test_gzip
from . import test_zipimport
from . import test_shutil
from . import test_tarfile_regressions
from . import test_zipfile_regressions
from . import test_lzma_regressions
from . import test_bz2_regressions
from . import test_gzip_regressions
from . import test_zipimport_regressions
from . import test_shutil_regressions
from . import test_tarfile_extra
from . import test_zipfile_extra
from . import test_lzma_extra
from . import test_bz2_extra
from . import test_gzip

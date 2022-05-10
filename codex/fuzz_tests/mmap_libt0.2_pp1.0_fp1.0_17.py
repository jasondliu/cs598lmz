import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib
import urllib2
import urlparse
import zipfile

from distutils.version import LooseVersion

from build_step import BuildStep, BuildStepWarning
from build_step_util import BuildStepUtil
from util import (
    ensure_directory_exists,
    get_file_hash,
    get_file_size,
    get_path_from_url,
    is_url,
    is_windows,
    is_zip_file,
    run_command,
    run_in_parallel,
    split_comma_separated_string,
    unzip,
    zip_directory,
)

# The maximum number of parallel downloads to perform.
MAX_PARALLEL_DOWNLOADS = 10

# The maximum number of parallel unzips to perform.
MAX_PARALLEL_UNZIPS = 10

# The maximum number of parallel commands to run.
MAX_PARALLEL_

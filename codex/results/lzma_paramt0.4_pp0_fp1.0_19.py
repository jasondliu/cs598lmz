from lzma import LZMADecompressor
LZMADecompressor()

import os
import sys
import argparse
import logging
import time
import subprocess
import threading
import multiprocessing
import multiprocessing.pool
import multiprocessing.managers
import queue
import math
import hashlib
import tempfile

# FIXME: this is a hack
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
from buildfarm.ros_distro import get_distribution_file, get_index, get_release_package_xmls
from buildfarm.rosdistro import get_cached_distribution_file
from buildfarm.release_job import get_repos_info

from rosdistro import get_index, get_distribution_file
from rosdistro import get_index_url, get_index_url_prefix
from rosdistro import get_source_build_files
from rosdistro import get_source_build_files_with_version
from rosdistro import get_source_build_file
from

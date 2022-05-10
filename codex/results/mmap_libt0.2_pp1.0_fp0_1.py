import mmap
import os
import re
import sys
import time

from collections import defaultdict
from datetime import datetime
from functools import partial
from itertools import chain
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from subprocess import Popen, PIPE

from . import __version__
from . import config
from . import exceptions
from . import utils
from . import vcs
from . import versioning
from . import versioning_utils
from .utils import (
    cached_property,
    get_logger,
    get_repo_root,
    get_version_from_tag,
    is_git_dir,
    is_hg_dir,
    is_svn_dir,
    is_version_tag,
    is_version_tag_dirty,
    is_version_tag_exists,
    is_version_tag_exists_remote,
    is_version_tag_remote,
    is_version_tag_remote_dirty,
    is_version_tag_remote_

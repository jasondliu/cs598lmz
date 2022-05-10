import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

from . import config
from . import context
from . import errors
from . import util
from . import vcs
from . import version
from . import version_sort
from .config import Config
from .context import Context
from .errors import UserError
from .util import (
    cached_property,
    ensure_dir,
    ensure_file,
    ensure_file_directory_exists,
    ensure_linked_file,
    get_env_var,
    get_files_in_dir,
    get_files_in_dir_by_ext,
    get_files_in_dir_by_name,
    get_files_in_dir_by_pattern,
    get_git_repo_root,
    get_git_repo_url,
    get_git_revision_hash,
    get_git_revision_short_hash,
    get_git_revision_timestamp,
    get_git_revision_timestamp_

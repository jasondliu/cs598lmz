import mmap
import os
import re
import sys

from collections import OrderedDict
from distutils.spawn import find_executable
from io import StringIO
from subprocess import Popen, PIPE

from . import __version__
from .utils import get_version_from_git, get_version_from_git_or_error
from .utils import get_version_from_git_or_unknown, get_version_from_git_or_none
from .utils import get_version_from_git_or_unknown_if_no_git
from .utils import get_version_from_git_or_unknown_if_no_git_or_hg
from .utils import get_version_from_git_or_unknown_if_no_git_or_hg_or_error
from .utils import get_version_from_git_or_unknown_if_no_git_or_hg_or_none
from .utils import get_version_from_git_or_unknown_if_no_git_or_hg_or_tag
from .utils import get_

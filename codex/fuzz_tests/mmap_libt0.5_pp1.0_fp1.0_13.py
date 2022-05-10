import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile

from . import config
from . import error
from . import log
from . import util
from . import version
from . import vcs
from . import vcs_git
from . import vcs_svn
from . import vcs_hg
from . import vcs_bzr
from . import vcs_fossil
from . import vcs_cvs
from . import vcs_darcs
from . import vcs_mtn
from . import vcs_arch
from . import vcs_tla
from . import vcs_pijul
from . import vcs_monotone

class Repo(object):
    def __init__(self, path, name=None, config=None, source=None,
                 source_type=None, source_name=None, source_options=None,
                 revision=None, branch=None, tag=None, depth=None,
                 clone_depth=None, clone_recursive=True,
                 use_mirrors=

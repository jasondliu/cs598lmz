import mmap
import os
import shutil
import struct
import tarfile
import tempfile
import zipfile

from . import log
from . import util
from . import vcs

from .build import BuildTarget
from .color import Color
from .compile import compile_1, compile_2
from .deps import get_deps, get_deps_1, get_deps_2
from .deps import get_transitive_deps_1, get_transitive_deps_2
from .error import CmdError
from .languages import get_language
from .platform import get_platform
from .process import Process
from .project import Project
from .timestamp import Timestamp
from .util import get_mtime
from .version import __version__

# ------------------------------------------------------------------------------

NAME = "b"

# ------------------------------------------------------------------------------

class Cmd(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(
                prog=NAME,
                description="Build and package your project using a single "
                        "configuration file.")

    def add_

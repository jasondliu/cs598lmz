import mmap
import os
import re
import subprocess
import sys
import time
import traceback

from . import config
from . import utils
from . import vcs
from . import xdg

class Project(object):
    """
    A project is a directory containing a .project file.
    """

    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.config = config.Config(os.path.join(path, '.project'))
        self.vcs = vcs.VCS(self)

    def __repr__(self):
        return '<Project %s>' % self.name

    def __str__(self):
        return self.name

    def __cmp__(self, other):
        return cmp(self.name, other.name)

    def __hash__(self):
        return hash(self.path)

    def __eq__(self, other):
        return self.path == other.path

    def __ne__(self, other):

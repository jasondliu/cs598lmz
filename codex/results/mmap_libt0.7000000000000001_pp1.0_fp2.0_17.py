import mmap
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

from six.moves import cStringIO as StringIO

from mercurial import (
    commands,
    error,
    localrepo,
    pycompat,
    scmutil,
    templates,
    ui as uimod,
)
from mercurial.utils import (
    procutil,
)

from hgsubversion import (
    util,
)

def maketemp():
    return tempfile.mkdtemp(prefix='hgsubversion-tests')

class SubversionRepo(object):
    def __init__(self, name):
        self.path = maketemp()
        self.name = name

        subprocess.call(['svnadmin', 'create', self.path],
                        stdout=subprocess.PIPE)
        self.svnurl = 'file://%s' % self.path

    def append_rev(self, rev, props=None):
        f = tempfile.

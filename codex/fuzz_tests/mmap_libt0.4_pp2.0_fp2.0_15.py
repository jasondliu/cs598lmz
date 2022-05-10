import mmap
import os
import sys
import tempfile
import unittest

from contextlib import contextmanager

from mercurial import (
    bookmarks,
    bundle2,
    changegroup,
    cmdutil,
    commands,
    discovery,
    error,
    exchange,
    extensions,
    hg,
    localrepo,
    lock,
    merge as mergemod,
    node,
    obsolete,
    phases,
    pycompat,
    repair,
    scmutil,
    smartset,
    store,
    subrepoutil,
    tags,
    templatekw,
    ui as uimod,
    util,
    vfs as vfsmod,
    worker,
)
from mercurial import (
    encoding,
    error,
    extensions,
    hg,
    localrepo,
    node,
    pycompat,
    scmutil,
    ui as uimod,
    util,
)
from mercurial.i18n import _

from . import (
   

import weakref
import filecmp
import shutil

from qumulo.lib.request import RequestError
from qumulo.lib.uri import Uri

try:
    from PyQt5 import QtGui, QtCore, QtWidgets
except ImportError:
    pass

import qumulo.lib.auth
import qumulo.lib.request
import qumulo.rest.file
import qumulo.rest.nfs
import qumulo.rest.share
import qumulo.rest.directory
import qumulo.lib.util
import qumulo.rest.quota
from qumulo.lib.uri import Uri


def path_to_policy(path):
    """Return human-readable path names.

    Strips leading slashes and replaces instances of / with \\.
    """
    path = path.strip('/')
    return re.sub(r'/', r'\\', path)



import types
# Test types.FunctionType below.

from syslog import syslog
import traceback

from pisi.specfile import SpecFile
from pisi.package import Package
from pisi.dependency import Dependency, PackageRelation
from pisi.util import partition, copyfile
from pisi.uri import URI
from pisi.atomicoperations import *
from pisi.actionsapi.runner import *
from pisi.actionsapi.shelltools import *
from pisi.actionsapi.kernel import *

# binary package builder

def install(package, destdir = None, keep_path = None, with_install_scripts = True, ignore_dep = False, params = None):
    """install package, at destdir if destdir is specified, otherwise
    in InstallDB.InstallDir

    @params: standard installation parameters can be specified, where
             the default one is "overwrite"
    """

    # change this (build directory) to destdir
    if destdir:
        config.destdir = destdir

    # expand environment variables in destdir
    config.destdir = os.path.expandvars(config

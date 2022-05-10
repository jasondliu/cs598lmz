import weakref
from copy import copy

from py.__.code.svncommands import run


class BuildException(Exception): pass


# If the BUILD_DATE is not set in the environment, then we calculate
# it and do not cache it.
BUILD_DATE = None
def get_build_date():
    global BUILD_DATE
    if BUILD_DATE is not None:
        return BUILD_DATE

    try:
        sys.path.insert(0, os.path.join(os.curdir, 'bin'))
        from pypy_buildbot import BUILD_DATE
    except ImportError:
        import time
        BUILD_DATE = time.gmtime()

    return BUILD_DATE


def get_build_tag():
    # The build tag is a string like 'r3271-2011-02-01-23-01'.
    # We use a local variable so that we do not have to cache
    # BUILD_DATE if the build tag has already been calculated.
    build_date = get_build_

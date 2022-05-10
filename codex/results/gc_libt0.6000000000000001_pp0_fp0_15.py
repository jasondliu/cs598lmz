import gc, weakref

from . import _compat
from . import _util

def pytest_addoption(parser):
    group = parser.getgroup('gcov')
    group.addoption('--gcov-source', action='store', default='.',
        help='path to the source directory')
    group.addoption('--gcov-output', action='store', default='.',
        help='path to the output directory')
    group.addoption('--gcov-exec', action='store', default=None,
        help='path to the gcov executable')
    group.addoption('--gcov-build-dir', action='store', default=None,
        help='path to the build directory')
    group.addoption('--gcov-prefix', action='store', default=None,
        help='prefix to prepend to source file paths')
    group.addoption('--gcov-extra-files', action='store', default=None,
        help='comma separated list of extra files to check')
    group.addoption('--gcov-xml', action='store', default=

import types
# Test types.FunctionType to determine if the callable is constructed with def
# or lambda, or if it's a partial.
import warnings

from ._path import abspath, normcase, exists
from . import _vendor
from . import _bootstrap
from ._bootstrap_external import Unicode
from . import _bootstrap_external
from . import _handle_fromlist
from ._bootstrap_external import ExtensionFileLoader
from ._bootstrap_external import ArchiveReader, zip_directory_cache
from ._bootstrap_external import _check_name_and_package
from ._bootstrap_external import (SOURCE_SUFFIXES, BYTECODE_SUFFIXES,
                                  EXTENSION_SUFFIXES)

from . import _imp

# Install import hooks for our C extensions
_bootstrap._install()

_verbose_message = '# clear builtin.{0!r}'.format

def _verbose_message_rev(name):
    return '# restore builtin.{0!r} from {0!r}'.format(name, '__multicall__')

def _get

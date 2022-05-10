import weakref

from . import _pyximport
from . import _pyximport_util

from . import _pyximport_importer

_pyximport_importer.install()

# For Python 2.6 and 2.7, we need to add the importer to the meta path
# explicitly.
import sys
if sys.version_info[:2] < (2, 7):
    sys.meta_path.append(_pyximport_importer)

# For Python 2.7 and 3.2, we need to add the importer to the path hook
# explicitly.
if sys.version_info[:2] < (2, 7):
    sys.path_hooks.append(_pyximport_importer)
elif sys.version_info[:2] == (2, 7) and sys.version_info[2] < 3:
    sys.path_hooks.append(_pyximport_importer)
elif sys.version_info[:2] == (3, 2):
    sys.path_hooks.append(_pyximport_importer)

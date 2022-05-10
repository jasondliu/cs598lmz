import weakref

from . import _imaging, _imagingmath, _imagingft

__version__ = "0.8.3"  # keep in sync with setup.py

try:
    from . import _webp
except ImportError as e:
    _webp = None

# These constants are defined in the _imaging C module.
DEFAULT_STRATEGY = 0

# FIXME: this is also defined in _imaging
MAXBLOCK = 1024

isPath = _imaging.isPath

# --------------------------------------------------------------------
# Declarations of standard _imaging objects


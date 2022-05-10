import weakref
from pathlib import Path
from typing import Dict, List, Union, Tuple, Optional, Any, Iterable

from .utils import Duration, to_path
from .exceptions import (
    ManifestError,
    ManifestNotFound,
    ManifestVersionError,
    ManifestParseError,
    ManifestMissingError,
    ManifestPermissionError,
    ManifestNotSelectedError
)

from .pack_index import PackIndex
from .profiles import Profile
from .profiles import ProfileNotFound


class ManifestNotFound(Exception):
    def __init__(self, *args, **kwargs):
        super(ManifestNotFound, self).__init__(*args, **kwargs)


class ManifestParseError(Exception):
    def __init__(self, *args, **kwargs):
        super(ManifestParseError, self).__init__(*args, **kwargs)



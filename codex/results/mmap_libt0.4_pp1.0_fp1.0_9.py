import mmap
import os
import re
import sys
import time
import traceback

from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

from . import config
from . import constants
from . import errors
from . import file_types
from . import log
from . import utils
from . import version
from . import xattr

# pylint: disable=too-many-instance-attributes,too-many-public-methods


class File:
    """Class representing a file.

    Attributes:
        path: File path.
        name: File name.
        dir_path: Directory path.
        size: File size.
        mtime: File modification time.
        ctime: File creation time.
        atime: File access time.
        mode: File mode.
        uid: File owner user id.
        gid: File owner group id.
        type: File type.
        type_str: File type string.
        ext: File extension.
        xattrs: File extended attributes.
        tags: File tags.
        mode

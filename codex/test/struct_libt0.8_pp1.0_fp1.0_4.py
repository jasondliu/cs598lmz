import _struct

import numpy as np
import os.path

from PIL import Image
from functools import wraps
from .puddle_objects import PuddleContext
from pypuddlestuff.puddleobjects import (
    _split_command, _get_icon, get_read_write)
from pypuddlestuff.constants import (
    VALID_TAGS, IMAGE_TAGS, IMAGE_TAG_REGEX_STR, PYPUDDLE_ROOT,
    NUMERIC_TAGS, EXTENSION_CACHE, WRITE_ERROR, READ_ERROR,
    WRITEFUNC_ERROR, READFUNC_ERROR)
from pypuddlestuff.util import get_extension, get_translation


import _struct
from datetime import datetime
from typing import List, Dict

import numpy as np

from pyxel.pack import Pack
from pyxel.pack.compression import compress
from pyxel.pack.encoding import get_varint_len, get_varint_bytes
from pyxel.pack.version import Version
from pyxel.types import Point, Size


# Common section format identifiers (1 byte).
_ID_NONE = 0
_ID_FILE_SIZE = 1
_ID_VERSION = 2
_ID_TILE_SIZE = 3
_ID_IMAGE_SIZE = 4
_ID_MUSIC_VOLUME = 5
_ID_SOUND_VOLUME = 6
_ID_IMAGE_COUNT = 7
_ID_TILE_COUNT = 8
_ID_SOUND_COUNT = 9
_ID_MUSIC_COUNT = 10
_ID_SOUND_DATA_SIZE = 11
_ID_MUSIC_DATA_SIZE = 12
_ID_LOGO_IMAGE_INDEX = 13
_ID

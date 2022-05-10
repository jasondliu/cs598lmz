import types
types.ModuleType.__dict__.__setitem__('__getattr__', lambda self, name: self.__getattribute__(name))

# noinspection PyUnresolvedReferences
import bpy
# noinspection PyUnresolvedReferences
import mathutils
# noinspection PyUnresolvedReferences
import math

# noinspection PyUnresolvedReferences
from io_scene_nif import nif_common
# noinspection PyUnresolvedReferences
from io_scene_nif import nif_import
# noinspection PyUnresolvedReferences
from io_scene_nif import nif_export
# noinspection PyUnresolvedReferences
from io_scene_nif import animation
# noinspection PyUnresolvedReferences
from io_scene_nif import nif_logging
# noinspection PyUnresolvedReferences
from io_scene_nif import nif_info
# noinspection PyUnresolvedReferences
from io_scene_nif import nif_utils
# noinspection PyUnresolvedReferences
from io_scene_nif import nif_

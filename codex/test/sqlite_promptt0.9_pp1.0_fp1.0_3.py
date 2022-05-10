import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
from os.path import isfile

if "bpy" in locals():
    import importlib
    if "gltf2_io_debug" in locals():
        importlib.reload(gltf2_io_debug)
    if "gltf2_io" in locals():
        importlib.reload(gltf2_io)
    if "gltf2_io_0100" in locals():
        importlib.reload(gltf2_io_0100)
    if "gltf2_io_visual_camera" in locals():
        importlib.reload(gltf2_io_visual_camera)
else:
    from . import gltf2_io_debug
    from . import gltf2_io
    from . import gltf2_io_0100
    from . import gltf2_io_visual_camera


from ..io.imp.gltf2_io_binary import BinReader, BinWriter
from ..blender.exp import gltf2_blender_export_keys


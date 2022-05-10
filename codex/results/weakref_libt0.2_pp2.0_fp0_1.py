import weakref

from . import _core
from . import _util
from . import _errors
from . import _types
from . import _lib
from . import _ffi
from . import _compat
from . import _thread
from . import _version

__all__ = ['connect', 'connect_tcp', 'connect_unix', 'connect_uds',
           'connect_xcb', 'connect_wayland', 'connect_osmesa',
           'connect_android_surface', 'connect_android_display',
           'connect_android_gpu', 'connect_android_gpu_display',
           'connect_android_gpu_display_sync', 'connect_android_gpu_display_sync_v2',
           'connect_android_gpu_display_sync_v3', 'connect_android_gpu_display_sync_v4',
           'connect_android_gpu_display_sync_v5', 'connect_android_gpu_display_sync_v6',
           'connect_android_gpu_display_sync_v7', 'connect_android_gpu_display_sync_v8',

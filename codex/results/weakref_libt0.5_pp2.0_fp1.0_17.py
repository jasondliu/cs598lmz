import weakref

from .. import _base
from .._base import _Libfreenect2Object
from ..enums import FrameType
from ..exceptions import FrameTypeError
from ..opencl import OpenCLDevice
from ..util import deprecate, to_string_buffer


class Frame(_Libfreenect2Object):
    """
    A frame from a :class:`~freenect2.SyncMultiFrameListener`.
    """

    _types = {}

    __slots__ = ("_frame", "_type", "_listener", "_listener_id")

    def __init__(self, frame, frame_type, listener, listener_id):
        self._frame = frame
        self._type = frame_type
        self._listener = weakref.ref(listener)
        self._listener_id = listener_id

    def __repr__(self):
        return "<{0} frame_type={1}>".format(self.__class__.__name__, self.frame_type)

    def __str__(self):
        return self.frame_type.name

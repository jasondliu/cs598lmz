import weakref

from . import _core
from ._core import _make_enum
from . import _util

#------------------------------------------------------------------------------
# Image
#------------------------------------------------------------------------------

class Image(_core.Image):
    """
    A class representing a single image.

    :param data: The data to initialize the image with.
    :type data: :class:`numpy.ndarray` or :class:`bytes`
    :param width: The width of the image.
    :type width: :class:`int`
    :param height: The height of the image.
    :type height: :class:`int`
    :param channels: The number of channels in the image.
    :type channels: :class:`int`
    :param format: The format of the image.
    :type format: :class:`Format`
    :param color_space: The color space of the image.
    :type color_space: :class:`ColorSpace`
    :param row_pitch: The row pitch of the image.
    :type row_pitch: :class:`int`
    :param

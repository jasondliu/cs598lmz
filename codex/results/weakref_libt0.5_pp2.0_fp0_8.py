import weakref

import numpy as np
from PIL import Image

from ..utils.logging import logger

__all__ = ['VideoReader']


class VideoReader(object):
    """A class that reads video files using FFmpeg.

    Parameters
    ----------
    filename : str
        Path to the video file.
    output_map : list of int
        Indices of channels to be returned.
    width : int
        Width of the frame to be returned.
    height : int
        Height of the frame to be returned.
    pix_fmt : str
        Pixel format of the frame to be returned.
    """
    def __init__(self, filename, output_map=None, width=None, height=None,
                 pix_fmt='rgb24'):
        self.filename = filename
        self.output_map = output_map
        self.width = width
        self.height = height
        self.pix_fmt = pix_fmt

        self._proc = None
        self._width = None
        self._height = None
        self

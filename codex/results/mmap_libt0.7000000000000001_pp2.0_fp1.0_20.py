import mmap
import os
import sys
import cv2

class MyProcessor(object):
    """
    A processor to read from a video file.
    """
    def __init__(self, filename):
        self._filename = filename
        # If a camera index is provided, open the video
        # stream from the camera, otherwise open a video file
        # with the provided filename
        self._cap = cv2.VideoCapture(filename)

        if not self._cap.isOpened():
            raise IOError('Error opening video file: "{}"'.format(filename))

        self._frame = None
        self._frame_count = -1
        self._frame_rate = self._cap.get(cv2.CAP_PROP_FPS)
        self._frame_width = int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self._frame_height = int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self._frame_channels = 3

    def next_frame(self):

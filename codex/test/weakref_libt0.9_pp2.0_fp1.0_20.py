import weakref
import itertools
import cv2
import sys

from PySide import QtGui, QtCore
from .viewer_gui import ViewerGui

from .utils import WeakType
from .threads import Task
from .panels.panel_pb2 import Panel
from .message import Message, MessageType

class ImageMode(Enum):
    Curved = 0
    Cylinder = 1
    Plane = 2

class Camera(object):
    def __init__(self):
        self.position = np.array([0, 0, 0], dtype=np.float32)
        self.rotation_matrix = np.eye(3, dtype=np.float32)

    @property
    def rotation_matrix_transpose(self):
        """
        :type: np.ndarray
        """
        return self.rotation_matrix.T

    @property
    def rotation_matrix_inverse(self):
        """
        :type: np.ndarray
        """

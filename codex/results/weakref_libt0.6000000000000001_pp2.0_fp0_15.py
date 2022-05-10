import weakref
import logging

# from multiprocessing import Process, Queue

import numpy as np
from PySide import QtGui, QtCore

from .. import core
from ..core import image_sequence
from ..core import image_sequence_factory
from ..core import image_sequence_types
from ..core import image_sequence_model
from ..core import image_sequence_view
from ..core import image_sequence_controller
from ..core import image_sequence_io


class ImageSequenceCell(object):
    def __init__(self, parent, item):
        self._parent = parent
        self._item = item
        self._image_sequence = None
        self._image_sequence_model = None
        self._image_sequence_controller = None
        self._image_sequence_view = None
        self._image_sequence_view_thread = None
        self._image_sequence_view_process = None
        self._image_sequence_view_process_queue = None
        self._image_sequence_view_process_queue_data = None
        self._image_sequence_view

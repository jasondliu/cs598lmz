import weakref
import time
import numpy as np

from pyglet import gl
from pyglet import graphics
from pyglet import clock

from openvision.visual.render import clear as default_clear
from openvision.drone_vision import drone
from openvision.drone_vision.drone import Drone

from openvision.drone_vision.processing.drawing import DrawingProcessor
from openvision.drone_vision.processing.events import EventProcessor
from openvision.drone_vision.processing.visualization import VisualizerProcessor

from openvision.drone_vision import logging
from openvision.drone_vision.logging import get_logger


class Vision2Viewer(object):
    """Vision2Viewer is the GUI manager of the Vision2 library.

    Vision2Viewer should be used to create the screen and manage the window.
    It is responsible for displaying the video feed and for drawing the shape
    detection, target detection and other processing results.

    Vision2Viewer should be subclassed if advanced functionality is needed.
    """


    def __init__(self,

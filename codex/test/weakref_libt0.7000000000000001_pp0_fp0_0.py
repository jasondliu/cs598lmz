import weakref
import sys

class Camera(object):
    """This class handles all types of camera and camera-like devices
    (e.g. a Video4Linux device, or a webcam)"""

    def __init__(self, device=None, name=None, backend=None,
                 size=(640,480), fps=15):
        self.device = device
        self.name = name
        self.backend = backend
        self.size = size
        self.fps = fps

        # This is used for the backend to store stuff
        self.backend_data = {}

        # This is used for the backend to store the actual fps
        self.__fps = 0

        self.backend_class = None
        self.backend_instance = None

        # Internal event used to signal that a frame is ready
        self._frame_ready = threading.Event()
        self._frame_ready.set()

        self.__dict__['frame'] = None

        self._time_before = 0
        self._time_after = 0
        self._time_elapsed = 0


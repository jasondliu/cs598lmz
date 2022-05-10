import _struct
from pygame.locals import *
from pygame import _view
from pygame.tests.test_utils import unittest
from pygame.tests.test_utils import example_path
from pygame.tests import test_utils
from pygame.tests.test_utils.test_runner_mixin import TestRunnerMixin


# sputs crashes on MinGW
_surface_unpack_color_crashes = (sys.platform == "win32"
                                 and sys.platform != "darwin")

try:
    _surface_uses_array = _surface.surfarray is not None  # noqa
except AttributeError:
    _surface_uses_array = False


class SurfaceTypeTest(unittest.TestCase):
    def test_Surface(self):
        """Ensure we can create a surface.

        The surface should fill with green
        """
        # This testcase fails on the following platforms:
        # * OSX -> It depends on the hardware. The default hardware possibly
        #   doesn't support the chosen format, but the test would pass on a
       

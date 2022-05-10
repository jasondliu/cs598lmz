import gc, weakref
from bibliopixel import LEDMatrix, LEDStrip
from bibliopixel.drivers.visualizer import DriverVisualizer
from bibliopixel.project import BaseTemplate
from bibliopixel import StripChannelTest, MatrixChannelTest
from bibliopixel.animation.strip import BaseStripAnim
from bibliopixel.animation.matrix import BaseMatrixAnim
import time

spath = lambda x: os.path.join(os.path.dirname(__file__), x)


class BPBaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = DriverVisualizer(8)
        self.driver.setMasterBrightness(255)
        self.driver.setFPS(20)

    def test_initialized(self):
        self.assertTrue(self.driver.numLEDs() == 8)
        self.assertTrue(self.driver._lastUpdate == 0)

    def test_init_and_teardown(self):
        self.assertTrue(self.driver.initialized is False)
        self.driver._init()

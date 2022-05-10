from bz2 import BZ2Decompressor
BZ2Decompressor.__init__ = lambda *args:\
        unittest.TestCase().assertTrue(True)
from src.core.core.recognizer import Recognizer
from src.tests.core.core.recognizer import tRecognizer

import matplotlib.pyplot as plot
#from mpl_toolkits.basemap import Basemap

class tRecognizer(unittest.TestCase, tRecognizer):

    def setUp(self):
        self.formatter = logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        self.file = logging.FileHandler(filename="testRecognizer.log")
        self.file.setLevel(logging.DEBUG)
        self.file.setFormatter(self.formatter)

        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.

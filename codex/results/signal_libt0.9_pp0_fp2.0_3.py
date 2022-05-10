import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

import os
import sys
import unittest
from glob import glob

from PyFoam.Infrastructure import lammpsLogParser
from PyFoam.Applications.LammpsscriptReader import LammpsscriptReader


class LammpsLogTest(unittest.TestCase):
    def testLogs(self):
        for log in glob(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),
                                     'logs',
                                     "*")):
            print("Testing", log)
            parser=lammpsLogParser(log)
            self.assertIsNotNone(parser[0])

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(LammpsLogTest("testLogs"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

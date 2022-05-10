import gc, weakref

import numpy as np

from spyndle import Epoch, Event
from spyndle.io import readFile, writeFile
from spyndle.io.edf import EDFWriter
from spyndle.io.edf.header import Header
from spyndle.io.edf.header import _EDFHeader
from spyndle.io.edf.header import _EDFPlusHeader

from spyndle.io.tests.test_edf import TestEDF

from spyndle.utils import check_file_exists

import os.path
import os

__version__ = "0.4.4-dev"

'''
This module is used to test the EDFWriter class.

Created on Nov 23, 2012
@author: T. Teijeiro
'''

class TestEDFWriter(TestEDF):
    '''
    Test class for the EDFWriter class.
    '''

    def setUp(self):
        '''
        Prepares a test directory for the tests.
        '''
        self.testdir =

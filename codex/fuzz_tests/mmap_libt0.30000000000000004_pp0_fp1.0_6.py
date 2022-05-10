import mmap
import os
import sys
import tempfile
import unittest

from pyfakefs import fake_filesystem_unittest

from ycm.tests import PathToTestFile
from ycmd.utils import ToBytes, ToUnicode
from ycmd import user_options_store
from ycmd.responses import NoExtraConfDetected
from ycmd.tests.test_utils import ( BuildRequest,
                                    ChunkMatcher,
                                    ErrorMatcher,
                                    LocationMatcher,
                                    MessageMatcher,
                                    RangeMatcher,
                                    SetUpApp,
                                    StopCompleterServer,
                                    WaitUntilCompleterServerReady )


class GetCompletions_Basic_test( fake_filesystem_unittest.TestCase ):

  def setUp( self ):
    self.maxDiff = None
    self.test_dir = PathToTestFile( 'testy' )
    self.SetUpApp( self.test_dir )
    self.request = {
      'filepath'  : PathToTestFile( 'testy', 'Get

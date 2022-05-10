import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import subprocess
import time
import urllib

from miro.plat import resources
from miro import app
from miro import prefs
from miro import util
from miro import feed
from miro import httpclient

from miro.test.framework import MiroTestCase, EventLoopTest
from miro.test import mock
from miro.plat.utils import (get_temp_filename, get_temp_directory,
        get_temp_video_filename, get_temp_audio_filename)

class TestUtil(MiroTestCase):
    def test_get_temp_filename(self):
        filename = get_temp_filename()
        self.assert_(os.path.exists(filename))
        self.assert_(os.path.isfile(filename))

    def test_get_temp_directory(self):
        directory = get_temp_directory()
        self.assert_(os.path.exists(directory))
        self.assert_(os.path.isdir(directory))

   

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
sys.path.append('../..')

import unittest

from TheNounProjectAPI.api import API
from TheNounProjectAPI.models import File
from TheNounProjectAPI.models import Icon
from TheNounProjectAPI.models import IconSet
from TheNounProjectAPI.models import Term
from TheNounProjectAPI.models import Upload
from TheNounProjectAPI.models import User

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.api = API(key='key', secret='secret')

    def test_get_icon_by_id(self):
        icon = self.api.get_icon_by_id(id=1)
        self.assertTrue(isinstance(icon, Icon))

    def test_get_icon_by_term(self):
        icon = self.api.get_icon_by_term(term='dog')
        self.assertTrue(isinstance(icon, Icon))

   

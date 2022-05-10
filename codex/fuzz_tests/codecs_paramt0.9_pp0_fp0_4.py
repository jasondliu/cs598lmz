import codecs
codecs.register_error('strict', codecs.ignore_errors)

import responses
from requests.auth import HTTPBasicAuth
import json

from cloud_snitch.mock import Mock


class TestRelease(unittest.TestCase):
    """Test Release class"""
    @classmethod
    def setUpClass(cls):
        cls.mock = Mock()
        cls.context = cls.mock.context()
        cls.local = cls.mock.local()
        cls.definitions = cls.mock.definitions()

    @classmethod
    def tearDownClass(cls):
        cls.mock.remove()
        del cls.mock

    def setUp(self):
        self.owner = 'testowner'
        self.repo = 'testrepo'
        self.branch = 'testbranch'
        self.path = '../my.groovy'
        self.ref = 'develop'
        self.tag = '0.0.1'
        self.job_url = 'https://server.com/

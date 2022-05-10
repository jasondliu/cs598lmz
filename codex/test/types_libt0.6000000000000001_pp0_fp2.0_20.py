import types
types.FunctionType = FunctionType

import unittest

import mock

from openstack.common import wsgi
from openstack.common.fixture import config
from openstack.common.middleware import request_id
from tests import utils


class RequestIDMiddlewareTest(unittest.TestCase):
    def setUp(self):
        super(RequestIDMiddlewareTest, self).setUp()

        self.config = config.Config()
        self.config(debug=True)
        self.config(use_syslog=False)

        self.mock_app = mock.Mock()
        self.middleware = request_id.RequestIdMiddleware(self.mock_app,
                                                         self.config)

    def test_process_request(self):
        class FakeRequest(object):
            environ = {}

        req = FakeRequest()
        self.middleware(req)
        self.assertTrue(req.environ.get('openstack.request_id'))


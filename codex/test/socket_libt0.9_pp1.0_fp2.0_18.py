import socket
import unittest

import cayley
import cayley.test.test_graph

class TestRestClient(unittest.TestCase):
    def assertRequest(self, request):
        """ Test if the request is done over a connection and the passed method is GET """
        self.assertEqual(request.method, 'GET')
        self.assertTrue(isinstance(request.connection, httplib.HTTPConnection))

    def test_httplib_connection(self):
        """ Test a simple GET request with httplib """
        graph = cayley.Graph(host="127.0.0.1", port=64210, calendar=calendar, http_client=httplib)

        with HTTMock(self.mock_get_request):
            graph.vertex("1")

        with HTTMock(self.mock_post_request):
            graph.set("1", "name", "foo")

    def test_without_calendar(self):
        """ Test a simple GET request without calendar """

import sys, threading
threading.Thread(target=lambda: sys.stdout.write('threading '), daemon=True).start()

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from twisted.internet.task import deferLater

from autobahn.twisted.util import sleep


class TestCase(unittest.TestCase):

    @inlineCallbacks
    def test_sleep_timeout(self):
        print('sleep_timeout ')
        res = yield sleep(0.1)
        self.assertEqual(res, None)

    @inlineCallbacks
    def test_sleep_cancel(self):
        print('sleep_cancel ')
        d = sleep(1)
        yield deferLater(reactor, 0.1, d.cancel)
        self.assertRaises(Exception, d.result)

    @inlineCallbacks
    def test_sleep_zero(self):
        print('sleep_zero ')
        res = yield sleep(0)
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.

import signal
# Test signal.setitimer not working on windows
from twisted.internet import reactor
from twisted.internet.task import LoopingCall

from test.util import build_grab, build_grab_transport
from test.util import BaseGrabTestCase
from test.server_util import BaseGrabServerTestCase
from test.tornado_util import TIMEOUT, TornadoTestCase
from test.util import GRAB_TRANSPORT
from test.util import TMP_FILE
from test.util import ignore_transport
from test.util import only_grab_transport
from test.util import only_transport


class TestRequest(BaseGrabTestCase):
    def setUp(self):
        self.server.reset()

    @ignore_transport('urllib3')
    def test_timeout(self):
        g = build_grab()
        g.setup(timeout=0.1)
        g.go(self.server.get_url())
        self.assertTrue(g.response.time > 0.1)


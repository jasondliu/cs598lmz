import signal
# Test signal.setitimer
class OTCP_CtrlC(unittest.TestCase):
    def _setitimer_handler(self, signal, frame):
        self.gotit = 1
    def _setitimer_handler(self, signum, frame):
        self.gotit = 1
    def _setitimer_handler(self, signum, frame):
        self.gotit = 1
    def test_setitimer(self):
        self.gotit = 0
        signal.signal(signal.SIGALRM, self._setitimer_handler)
        """
        signal.SIGALRM
        signal.ITIMER_REAL
        signal.ITIMER_VIRTUAL
        """
        signal.setitimer(signal.ITIMER_REAL, 1, 0)
        #while not self.gotit: pass
        #time.sleep(1)
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

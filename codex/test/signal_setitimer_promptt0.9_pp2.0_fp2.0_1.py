import signal
# Test signal.setitimer
def catch_alarm(*args):
    '''Called on SIGALRM'''
    print_error("Caught alarm!")

class Test_signal(unittest.TestCase):
    def test_INT(self):
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        os.kill(os.getpid(), signal.SIGINT)
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    def test_ALRM(self):
        if sys.platform not in ('win32', 'cygwin'):
            signal.signal(signal.SIGALRM, catch_alarm)
            signal.signal(signal.SIGALRM, signal.SIG_IGN) # No effect
            self.assertRaises(ValueError, signal.signal, signal.SIGALRM, 42)
            self.assertTrue(signal.getsignal(signal.SIGALRM) is signal.SIG_DFL)

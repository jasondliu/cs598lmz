import threading
# Test threading daemon.
from test_threading_local import target, ThreadingLocalTest

class ThreadingDaemonTest(ThreadingLocalTest):

    # Tests using a non-daemon thread of Threading.local objects.

    def non_daemon_thread(self):
        ThreadingLocalTest.non_daemon_thread(self)
        self.local.x = 42

    def test_non_daemon_thread(self):
        self.local = self.Local()
        thread = threading.Thread(target=self.non_daemon_thread)
        thread.start()
        thread.join()
        self.assertTrue(self.local is thread.local)
        self.assertTrue(getattr(self.local, "x", None) is None)

    # Tests using a daemon thread of Threading.local objects.

    def daemon_thread(self):
        ThreadingLocalTest.daemon_thread(self)
        self.local.x = 42

    def test_daemon_thread(self):
        self.local = self.Local()
        thread = threading.Thread(

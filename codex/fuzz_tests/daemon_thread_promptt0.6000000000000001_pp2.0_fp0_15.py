import threading
# Test threading daemon
# Test threading join
# Test threading start
# Test threading stop
# Test threading wait
# Test threading running
# Test threading alive
# Test threading terminate
# Test threading pause
# Test threading resume
# Test threading restart
# Test threading is_daemon
# Test threading is_alive
# Test threading is_running
# Test threading is_paused
# Test threading is_stopped
# Test threading is_terminated
# Test threading is_started
# Test threading is_waiting

class TestThreading(unittest.TestCase):

    def setUp(self):
        self.thread = threading.Thread(target=self.thread_sleep_3)
        self.thread.daemon = True
        self.thread.start()

    def tearDown(self):
        self.thread.terminate()
        self.thread.wait()

    def thread_sleep_3(self):
        time.sleep(3)

    def test_threading_daemon(self):
        self.assertEqual(

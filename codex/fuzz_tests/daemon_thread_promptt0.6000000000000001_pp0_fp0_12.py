import threading
# Test threading daemon mode.

class ThreadingTest(unittest.TestCase):
    def test_daemon_threading(self):
        def thread_func():
            time.sleep(1.2)
        t = threading.Thread(target=thread_func)
        t.daemon = True
        t.start()
        start_time = time.time()
        t.join()
        self.assertAlmostEqual(time.time() - start_time, 1.0, delta=0.5)

if __name__ == '__main__':
    unittest.main()

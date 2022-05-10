import threading
# Test threading daemon
class thread_mockz(threading.Thread):
    def run(self):
        for x in range(0, 70):
            print x
            time.sleep(2)
# End test

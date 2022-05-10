import threading
# Test threading daemon. Using daemon to avoid thread block main thread when executing main thread close.
class TestThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.flag = True

    def run(self):
        while True:
            if self.flag:
                print('Tick')
                time.sleep(1)
            else:
                print('exit')
                break

    def stop(self):
        print('stop')
        self.flag = False
# Main Entrance
if __name__ == "__main__":
    # Init
    t = TestThread()
    t.daemon = True
    try:
        t.start()
        # Do your stuff
        while True:
            # handling input
            var_input = input("Type quit to quit\n")
            if var_input.lower() == "quit":
                t.stop()
                break
    except Exception as e:
        print(e)

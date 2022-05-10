import threading
# Test threading daemon
# See http://docs.python.org/library/threading.html

# This program will print out the current time every second but will
# not exit until you press ctrl+c.
# Note that this is a daemon thread.

class Poller:
    def __init__(self):
        self.interval = 1.0
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        while True:
            # Do something
            print(datetime.datetime.now())
            time.sleep(self.interval)

p = Poller()

while True:
    time.sleep(10)
    print("Main thread working...")

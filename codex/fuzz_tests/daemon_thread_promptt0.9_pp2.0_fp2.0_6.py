import threading
# Test threading daemon
import time


def daemon():
    # Set daemonizing, this blocks main thread
    daemon_thread = threading.currentThread()
    print daemon_thread.getName(), "Starting"
    time.sleep(2)
    print daemon_thread.getName(), "Exiting"


# Threading
d = threading.Thread(name="daemon", target=daemon)
d.setDaemon(True)

# Start daemoning
d.start()
d.join()

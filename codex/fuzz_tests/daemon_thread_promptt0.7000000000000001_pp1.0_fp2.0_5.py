import threading
# Test threading daemon

# =============================
#   Global variables
# =============================

g_quit = False

# =================================
#   Thread class
# =================================

class ThreadClass(threading.Thread):
    def __init__(self):
        super(ThreadClass, self).__init__()
        self.daemon = True # Daemon mode

    def run(self):
        global g_quit
        print("Thread start: daemon=", self.daemon)
        while not g_quit:
            time.sleep(1)
        print("Thread stop: daemon=", self.daemon)

# =================================
#   Main
# =================================

def main():
    global g_quit

    # Create thread
    thread = ThreadClass()

    # Start Daemon thread
    thread.start()

    # Sleep 10 secs
    time.sleep(10)

    # Stop
    g_quit = True

    # Wait
    thread.join()

    # Sleep 3 secs
    time.sleep(3)

if __name__ == "__main__":
    main()

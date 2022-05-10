import threading
# Test threading daemon
# daemon: a thread that runs in the background without tying up the user interface
def daemon():
    print("Start daemon")
    time.sleep(5)
    print("Exit daemon")

if __name__ == "__main__":
    # If the attribute is set to True, the daemonizer (thread) will get killed when the main thread terminates
    d = threading.Thread(name="daemon", target=daemon)
    d.setDaemon(True)

    # Start the thread
    d.start()

    # Make sure all threads complete
    # join() blocks until the thread terminates
    d.join()

    print("All done")

import threading
# Test threading daemon
def test(name):
    for i in range(10):
        print(name, ":", i)
        time.sleep(1)

# Create the thread
daemon = threading.Thread(target=test, args=("Daemon", ))
daemon.setDaemon(True)

# Create another thread
thread = threading.Thread(target=test, args=("Thread", ))

# Start both threads
daemon.start()
thread.start()

# Wait only for the non-daemon thread
thread.join()
print("Finished")

# Print if the daemon is alive
if daemon.isAlive():
    print("Daemon is still running")
else:
    print("Daemon is dead")

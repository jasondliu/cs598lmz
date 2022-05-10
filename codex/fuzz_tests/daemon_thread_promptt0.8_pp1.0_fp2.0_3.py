import threading
# Test threading daemon properties
#
# Demonstrates:  thread, daemon, join
#
# Author: David Campbell
# Date:   April 2015
#
#
# To run:
#
#   $python daemon.py
#

def daemon_worker():
    """Worker thread in daemon mode"""
    while True:
        print("Hello from daemon thread.")
        time.sleep(2)

# Main thread
print("Main thread starting...")

d = threading.Thread(name="daemon_thread", target=daemon_worker)
d.daemon = True
d.start()
print("Main thread is continuing...")
d.join()

print("Main thread exiting.")

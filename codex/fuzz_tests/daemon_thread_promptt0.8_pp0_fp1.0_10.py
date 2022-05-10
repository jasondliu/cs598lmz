import threading
# Test threading daemonize

def run():
    while True:
        print("thread running")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.setDaemon(True)
thread.start()

while True:
    pri

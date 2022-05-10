import threading
# Test threading daemon
def worker():
    print("Enter worker")
    time.sleep(2)
    print("leave worker")
t = threading.Thread(target=worker)
t.setDaemon(True)
t.start()

# Result:
# Enter worker
# leave worker
# main thread exit

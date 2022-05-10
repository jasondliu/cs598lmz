import threading
# Test threading daemon
def worker():
    while True:
        print("hello")
        time.sleep(1)

d = threading.Thread(name='daemon', target=worker)
d.setDaemon(True)
d.start()
d.join()

print("Done")

# Test threading with return
def worker():
    return

t = threading.Thread(name='non-daemon', target=worker)
t.daemon = True
t.start()
t.join()

print("Done")

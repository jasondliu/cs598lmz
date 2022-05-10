import threading
# Test threading daemon

class ThreadClass(threading.Thread):
    def run(self):
        for i in range(5):
            print("Running")
            time.sleep(1)

t = ThreadClass()
t.start()
time.sleep(6)
print("Is Alive:", t.is_alive())

# Test threading daemon

class ThreadClass(threading.Thread):
    def run(self):
        for i in range(5):
            print("Running")
            time.sleep(1)

t = ThreadClass()
t.setDaemon(True)
t.start()
time.sleep(6)
print("Is Alive:", t.is_alive())

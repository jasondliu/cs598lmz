import threading
# Test threading daemon
def worker():
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()

raw_input("Press Enter to continue...")

# Test threading daemon with shared global variable
def worker():
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()

raw_input("Press Enter to continue...")

# Test threading daemon with shared global variable
def worker():
    global x
    x = x + 1
    print('Worker')
    return

threads = []
x = 0
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
for thread in threads:

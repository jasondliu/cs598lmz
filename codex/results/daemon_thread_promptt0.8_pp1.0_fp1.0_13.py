import threading
# Test threading daemon
count = 0
def adder(addlock):
    global count
    with addlock:
        count = count + 1
    time.sleep(0.5)
    with addlock:
        count = count + 1
threads = []
for i in range(100):
    thread = threading.Thread(target=adder,args=(threading.Lock(),))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print(count)

count = 0
addlock = threading.Lock()
def adder(addlock):
    global count
    with addlock:
        count = count + 1
    time.sleep(0.5)
    with addlock:
        count = count + 1
threads = []
for i in range(100):
    thread = threading.Thread(target=adder,args=(addlock,))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print(count)

count = 0
threadLock = threading.Lock()

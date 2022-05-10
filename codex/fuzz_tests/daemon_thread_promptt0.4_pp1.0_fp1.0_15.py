import threading
# Test threading daemon

def worker():
    print('worker')
    time.sleep(2)
    print('worker')

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('main thread')

# Test threading daemon
# daemon = True
# 当主线程退出时，子线程kill掉

def worker():
    print('worker')
    time.sleep(2)
    print('worker')

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('main thread')

# Test threading daemon
# daemon = True
# 当主线程退出时

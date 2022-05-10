import threading
# Test threading daemon
"""
def f(n):
    while True:
        print('Thread %s\n' % n)
        time.sleep(1)

for n in range(5):
    t = threading.Thread(target=f, args=(n,))
    t.setDaemon(True)
    t.start()

while True:
    time.sleep(0.5)
"""

# Test threading
# Blocking call.
"""
def f():
    print('thread function')
    return

if __name__ == '__main__':
    t = threading.Thread(target=f)
    t.start()
    t.join()
    print('thread over')
"""

# Test threading
# Non-blocking call

def f():
    print('thread function')
    return

if __name__ == '__main__':
    t = threading.Thread(target=f)
    t.start()
    # t.join()
    print('thread over')

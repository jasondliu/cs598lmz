import threading
# Test threading daemon

def f():
    print('thread function')
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f)
        t.setDaemon(True)
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        print(t.getName())
        # t.join()
    print('main_thread')

# Test threading lock

def f():
    global num
    temp = num
    time.sleep(0.001)
    num = temp - 1

num = 100
thread_list = []
for i in range(100):
    t = threading.Thread(target=f)
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

print('num:', num)

# Test threading lock

num = 100
lock = threading.Lock()


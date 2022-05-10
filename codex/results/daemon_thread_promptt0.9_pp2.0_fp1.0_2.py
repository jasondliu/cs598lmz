import threading
# Test threading daemon

def foo(x):
    print("foo",x)
    # time.sleep(1)

# t1 = threading.Thread(target=foo, args=(5,))
# t1.daemon = True
# t1.start()
# t2 = threading.Thread(target=foo, args=(5,))
# t2.daemon = False
# t2.start()

daemon_threads = []

for i in range(3):
    t = threading.Thread(target=foo, args=(i,))
    t.daemon = True
    thread.daemon_threads.append(t)

for thread in daemon_threads:
    thread.start()
    # print("thread.is_alive()",thread.is_alive())

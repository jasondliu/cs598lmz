import threading
threading.stack_size(67108864)

def run_thread(n):
    print("thread %s" % n)
    for i in range(1000000):
        x = i * i

for i in range(4):
    t = threading.Thread(target=run_thread, args=(i,))
    t.start()

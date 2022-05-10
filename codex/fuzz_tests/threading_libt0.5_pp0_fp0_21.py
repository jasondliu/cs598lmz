import threading
threading.stack_size(2 ** 27)

def run_thread(n):
    print("thread ", n)

threads = []
for i in range(5):
    t = threading.Thread(target=run_thread, args=(i,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("thread example finished")

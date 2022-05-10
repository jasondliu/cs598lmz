import threading
threading.stack_size(67108864)


def worker():
    print('Worker')
    return


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for i in range(5):
    threads[i].join()

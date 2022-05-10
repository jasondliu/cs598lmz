import sys, threading

def run():
    for i in range(10):
        print(threading.current_thread().name, i)
        time.sleep(0.1)

threads = []
for i in range(5):
    t = threading.Thread(target=run)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('main thread ends')

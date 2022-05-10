import sys, threading

def run():
    print(threading.current_thread().getName())
    for i in range(10):
        print(i)
        time.sleep(0.1)

threads = []

for i in range(5):
    t = threading.Thread(target=run, name='Thread-{}'.format(i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(threading.current_thread().getName())

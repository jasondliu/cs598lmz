import sys, threading

def run():
    for i in range(500):
        print(threading.current_thread().getName() + " " + str(i))

threads = []

for i in range(5):
    t = threading.Thread(target=run)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

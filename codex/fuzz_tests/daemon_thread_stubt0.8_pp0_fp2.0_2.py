import sys, threading

def run():
    for i in range(2):
        sys.stdout.write("hello from thread %d\n" % i)

threads = []
for i in range(5):
    t = threading.Thread(target=run)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

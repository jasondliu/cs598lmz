import sys, threading

def run():
    sys.stdout.write(str(threading.currentThread().getName())+'\n')
    sys.stdout.flush()
    return

threads = []
for i in range(5):
    t = threading.Thread(target=run)
    threads.append(t)
    t.start()

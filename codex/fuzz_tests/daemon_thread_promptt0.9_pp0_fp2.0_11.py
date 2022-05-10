import threading
# Test threading daemon mode which should terminate all threads when the
# main thread is terminated

def worker(cv, i):
    print('%s: starting' % i)
    cv.wait()
    print('%s: finishing' % i)

def daemon(cv):
    print('d: started')
    cv.wait()
    print('d: finished')

cv = threading.Condition()
p = [threading.Thread(target=worker, args=(cv,j)) for j in range(3)]
d = threading.Thread(target=daemon, args=(cv,))
d.setDaemon(True)

for i in p:
    i.start()
d.start()

time.sleep(0.1)

with cv:
    cv.notify_all()

time.sleep(0.1)

print('---------------')

for i in p:
    i.join()

time.sleep(1)

print('---------------')

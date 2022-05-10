import threading
# Test threading daemon mode
def run(n):
    print('[%s]\t: %s' %(threading.current_thread(), n))
    time.sleep(2)

t1 = threading.Thread(target=run, args=('t1',))
t2 = threading.Thread(target=run, args=('t2',))

t1.setDaemon(True)
t2.setDaemon(True)

t1.start()
t2.start()

t1.join()
t2.join()

print('done')

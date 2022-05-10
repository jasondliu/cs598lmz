import threading
# Test threading daemon
def t():
    while 1:
        print 'threading'
        time.sleep(2)
threading.Thread(target=t).setDaemon(True)
while 1:
    print 'Main threading'
    time.sleep(1)

# Test threading daemon 2
def run():
    while True:
        print 'thread %s is running...' % threading.current_thread().name
        time.sleep(1)


print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=run, name='MyThread')
t.setDaemon(True)
t.start()
print 'thread %s ended.' % threading.current_thread().name

import threading
# Test threading daemon
#
#

def daemon_thread(n, dt):
    while True:
        print '%s: %s' % (n, time.ctime())
        time.sleep(dt)

def non_daemon_thread(n, dt):
    while True:
        print '%s: %s' % (n, time.ctime())
        time.sleep(dt)


d = threading.Thread(name='daemon',
                     target=daemon_thread,
                     args=('daemon', 2))
d.setDaemon(True)

t = threading.Thread(name='non-daemon',
                     target=non_daemon_thread,
                     args=('non-daemon', 2))

d.start()
t.start()

#d.join()
t.join()
print 'end'

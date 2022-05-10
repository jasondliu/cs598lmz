import threading
# Test threading daemon
#
#
def worker():
    while True:
        print('worker')
        time.sleep(1)

t = threading.Thread(target=worker)
t.setDaemon(True)
t.start()

print('main thread')
#time.sleep(5)

# Test threading.local
#
#
#local_obj = threading.local()
#
#def worker():
#    local_obj.x = 1
#    print('worker local_obj.x = ', local_obj.x)
#    local_obj.x += 1
#    print('worker local_obj.x = ', local_obj.x)
#
#t = threading.Thread(target=worker)
#t.start()

# Test threading lock
#
#
#lock = threading.Lock()
#
#def worker():
#    with lock:
#        print('worker')
#
#t = threading.Thread(target=worker)
#t.start()
#
#with lock:
#    print('main thread')



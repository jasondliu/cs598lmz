import threading
# Test threading daemon thread
def daemon():
    print ('Starting:',threading.current_thread().name)
    time.sleep(2)
    print ('Exiting :',threading.current_thread().name)

def non_daemon():
    print ('Starting:',threading.current_thread().name)
    print ('Exiting :',threading.current_thread().name)
d2 = threading.Thread(name='non-daemon', target=non_daemon)
d2.setDaemon(False)
d1 = threading.Thread(name='daemon', target=daemon)
d1.setDaemon(True)
d3 = threading.Thread(name='daemon2', target=daemon)
d3.setDaemon(True)
d2.start()
d1.start()
d3.start()

# print (d2.isDaemon())
# print (d1.isDaemon())

print('d1.isAlive() = {}'.format(d1.isAlive()))
print('d2.isAlive() = {}

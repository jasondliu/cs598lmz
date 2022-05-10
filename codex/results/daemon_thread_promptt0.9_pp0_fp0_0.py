import threading
# Test threading daemon
# where daemon threads are not allowed to block,


import threading, logging, time

def daemon():
	logging.debug('Start')
	time.sleep(0.2)
	logging.debug('Exit')

def non_daemon():
	logging.debug('Start')
	logging.debug('Exit')

logging.basicConfig(level=logging.DEBUG,	format='(%(threadName)-10s) %(message)s',)

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join(22)
print 'd.isAlive()', d.isAlive()
t.join()

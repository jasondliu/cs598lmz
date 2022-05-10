import threading
# Test threading daemon
def daemon():
	print('Start daemon thread')
	time.sleep(1)
	print('End daemon thread')
d=threading.Thread(target=daemon)
d.setDaemon(True)
d.start()
d.join()

# Test non-daemon threading
def non_daemon():
	print('Start non-daemon thread')
	time.sleep(1)
	print('End non-daemon thread')
n=threading.Thread(target=non_daemon)
n.setDaemon(False)
n.start()
n.join()

print('End of main thread')

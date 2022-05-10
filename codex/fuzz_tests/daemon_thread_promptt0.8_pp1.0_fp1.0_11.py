import threading
# Test threading daemon
def Log():
	while True:
		time.sleep(1)
		print 'hello'
		
def Test():
	time.sleep(5)
	print 'world'
	
if __name__ == '__main__':
	t1=threading.Thread(target=Log)
	t2=threading.Thread(target=Test)
	# t1.setDaemon(True)
	t1.start()
	t2.start()

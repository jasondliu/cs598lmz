import threading
threading.currentThread().setName('mainThread')

try:
	server()
except KeyboardInterrupt:
	exit()
except:
	pass

import sys, threading

def run():
	global counter, lock
	while True:
		lock.acquire()
		if counter < 10:
			counter += 1
			print counter
		lock.release()
		time.sleep(0.5)

lock = threading.Lock()
counter = 0

t = threading.Thread(target=run)
t.setDaemon(1)
t.start()

while True:
	pass

'''

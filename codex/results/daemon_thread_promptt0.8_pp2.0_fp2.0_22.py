import threading
# Test threading daemon mode
# When app is exit, threads in daemon mode will be killed as well

# Create threading object
mu = threading.Lock()
lock = threading.Condition()

def threadingDaemon(name, delay, repeat):
	# print("Start threading: " + name)
	while repeat >= 0:
		time.sleep(delay)
		mu.acquire()
		lock.acquire()
		print("{} {}".format(name, time.ctime(time.time())))
		lock.release()
		mu.release()
		repeat -= 1

def main():
	thread1 = threading.Thread(target=threadingDaemon, args=("Thread1", 1.5, 5))
	thread2 = threading.Thread(target=threadingDaemon, args=("Thread2", 2.5, 5))

	thread1.setDaemon(True)
	thread2.setDaemon(True)

	thread1.start()
	thread2.start()
	print("Exiting main thread")

if __name__

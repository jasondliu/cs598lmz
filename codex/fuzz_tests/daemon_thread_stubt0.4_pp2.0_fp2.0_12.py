import sys, threading

def run():
	print("Thread 1: starting")
	time.sleep(0.5)
	print("Thread 1: finishing")

def run2():
	print("Thread 2: starting")
	time.sleep(0.5)
	print("Thread 2: finishing")

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Thread finished...exiting")

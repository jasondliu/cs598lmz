import threading
# Test threading daemon
def loop1():
	global balance
	balance = balance + 1
	balance = balance - 1

# b = balance
# threads = []
# for i in range(100000):
# 	t = threading.Thread(target = loop1)
# 	threads.append(t)

# for t in threads:
# 	t.start() # Run threads

# for t in threads:
# 	t.join() # Wait threads finishing

# print(balance)

# multi-threading
balance = 0
lock = threading.Lock()

def run_thread(n):
	for i in range(100000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2

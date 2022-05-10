import threading
# Test threading daemon
import _thread

# Message queue
import queue

# This is global variable
g_queue = queue.Queue()

def threading_func():
	for i in range(1, 11):
		g_queue.put(i)
		print(i)
		time.sleep(0.1)

print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread())

t = threading.Thread(target = threading_func)
t.start()
t.join()
print("Finished")

print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread())

print("----------------------------------------")

def threading_input(name):
	for i in range(1, 11):
		g_queue.put(i)
		print(name, g_queue.get())
		time.sleep(0.1)

# Create thread
# threading_input("Receiver")
# _thread.start_new

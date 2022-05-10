import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect('/home/xuying/Desktop/test.db')
c = conn.cursor()
c.execute("SELECT * FROM test")
print(c.fetchall())

# Test ctypes cdll
libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.printf("Hello, %s!\n", b"world")

# Test threading
def print_time(thread_name, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print ("%s: %s" % ( thread_name, time.ctime(time.time()) ))

try:
	thread.start_new_thread( print_time, ("Thread-1", 2, ) )
	thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
	print ("Error: unable to start thread")

while 1:
	pass

import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute(''' CREATE TABLE voters (name TEXT, votes INT)''')
print(sqlite3.version)

# Test ctypes.cdll.LoadLibrary()

libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
libc.time()

# Test threading.Thread

class MyThread(threading.Thread):
  def __init__(self, threadID, name):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
  def run(self):
    print('Thread: ' + self.name)
    print('Thread ID: ' + str(self.threadID))

thread1 = MyThread(1, 'Thread1')
thread2 = MyThread(2, 'Thread2')

thread1.start()
thread2.start()

print('Exiting Main Thread')

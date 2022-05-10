import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#conn = sqlite3.connect('test.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#conn.commit()
#conn.close()

# Test ctypes.util.find_library
#print ctypes.util.find_library('c')

# Test threading.Thread
#class MyThread(threading.Thread):
#    def __init__(self, thread_id, name, counter):
#        threading.Thread.__init__(self)
#        self.thread_id = thread_id
#        self.name = name
#        self.counter = counter
#    def run(self):
#        print "Starting " + self.name
#        print_time(self.name, self.counter, 5)
#        print "Exiting " + self.name
#
#

import threading
# Test threading daemon mode - notice that this usage also exists in
# cookbook/daemon.py, but it is not the focus of that recipe
# Task: Output Hello World every 0.5 seconds
import time
import datetime

class Hello(threading.Thread):
    def run(self):
        while True:
            print 'Hello World, today is the last day of the year :(', datetime.datetime.now().strftime('%H:%M:%S')
            time.sleep(0.5)


t = Hello()
t.daemon = True
t.start()
time.sleep(10)

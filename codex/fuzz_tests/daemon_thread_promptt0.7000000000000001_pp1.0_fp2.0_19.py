import threading
# Test threading daemon
import time

def worker():
    while True:
        print("worker")
        time.sleep(1)

t = threading.Thread(target=worker)
t.setDaemon(True)
t.start()

# main thread
while True:
    print("main")
    time.sleep(1)

# Using logging
import logging

logging.basicConfig(filename="/tmp/test.log", level=logging.DEBUG)
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

# simple example
import threading
import logging

def worker():
    logging.debug("starting")
    time.sleep(2)
    logging.debug("end")

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")
t = threading.Thread(target=worker, name="test")
t.start()

# threading and logging
import threading

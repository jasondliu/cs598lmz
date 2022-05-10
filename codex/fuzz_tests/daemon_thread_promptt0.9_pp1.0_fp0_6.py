import threading
# Test threading daemon
def f():
    while(1):
        pass

def g():
    while(1):
        print("g")
    return
t1 = threading.Thread(target = f)
t1.daemon = True
t2 = threading.Thread(target = g())
t2.daemon = True
t1.start()
t2.start()
t2.join()

# Answer
# t1 terminate immediately when t2 finished
# because t1.daemon = True

# Question
# Use logging module for print
import logging
def get_logger():
    logging.basicConfig(filename="logger.log", level=logging.INFO)
    logger = logging.getLogger()
    return logger

# Answer
# Add logger.info() to print
# What is level
# level=logging.DEBUG ===> debug information
# level=logging.INFO ===> system information
# level=logging.WARN ===> warning information
# level=logging.4RROR ===> error information
# level=logging.CRITICAL ===> critical information


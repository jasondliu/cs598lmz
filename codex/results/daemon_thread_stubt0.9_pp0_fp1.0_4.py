import sys, threading

def run():
    sys.exit(7)

t = threading.Thread(target=run)
t.start()
t.join()

#-------------------------------------------------
print('-'*50)
#-------------------------------------------------

import sys, threading, time

def run(x=None, y=None):
    sys.exit(7)

t = threading.Thread(target=run, args=(4, 5))
t.start()
t.join()

#-------------------------------------------------
print('-'*50)
#-------------------------------------------------


import sys, threading, time

def run(x=None, y=None):
    time.sleep(1)
    sys.exit(7)

t = threading.Thread(target=run, args=(4, 5))
t.start()
t.join()



#-------------------------------------------------
print('-'*50)
#-------------------------------------------------

import sys, threading, time

def run(x=None, y=None):
    time.sleep(1)
    sys.exit(7)

t = threading.Thread(target=run

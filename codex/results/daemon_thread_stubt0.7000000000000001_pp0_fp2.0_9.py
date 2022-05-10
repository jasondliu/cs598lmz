import sys, threading

def run():
    while True:
        print "Hello"
    
def run2():
    while True:
        print "Goodbye"
    
    

t = threading.Thread(target=run)
t2 = threading.Thread(target=run2)
t.start()
t2.start()

t.join()

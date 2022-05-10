import sys, threading

def run():
    print "bob"
    threading.Timer(1.0, run).start()
    
if __name__ == "__main__":
    threading.Timer(1.0, run).start()

    while True:
        pass

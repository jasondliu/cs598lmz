import sys, threading

def run():
    sys.exit(0)

def run2():
    sys.exit(1)

t = threading.Thread(target=run)
t.start()

t = threading.Thread(target=run2)
t.start()

#pythran export test()
def test():
    return 0

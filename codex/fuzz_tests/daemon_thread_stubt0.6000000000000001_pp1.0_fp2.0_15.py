import sys, threading

def run():
    raw_input()
    sys.exit()

t = threading.Thread(target=run)
t.start()

print 'hello'
t.join()

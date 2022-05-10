import sys, threading

def run():
    print 'Thread started'
    sys.exit(0)

thread = threading.Thread(target=run)
thread.start()
thread.join()

print 'Thread finished'

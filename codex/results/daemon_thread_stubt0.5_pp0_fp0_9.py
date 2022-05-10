import sys, threading

def run():
    print 'Thread started!'
    time.sleep(1)
    print 'Bye bye!'

threading.Thread(target=run).start()

print 'Main thread sleeping for 2 seconds'
time.sleep(2)

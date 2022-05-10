import sys, threading

def run():
    while True:
        sleep(1)
        print 'thread'

threading.Thread(target=run).start()

print 'main'

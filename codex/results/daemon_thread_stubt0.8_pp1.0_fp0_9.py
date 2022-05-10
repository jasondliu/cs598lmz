import sys, threading

def run():
    i = 0
    while True:
        print('thread%d' % i)
        time.sleep(1)
        i += 1

t = threading.Thread(target=run, name='Thread-1')
#t.setDaemon(True)
t.start()
pass

while True:
    pass

import sys, threading

def run():
    print('start')
    time.sleep(1)
    print('end')

t = threading.Thread(target=run)
t.daemon = True
t.start()

time.sleep(3)
print('main')

import sys, threading

def run():
    for i in range(10):
        print(i)
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    try:
        time.sleep(1)
        print('Main thread')
    except KeyboardInterrupt:
        sys.exit()

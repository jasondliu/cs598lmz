import sys, threading

def run():
    for i in range(10):
        print(i)
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    time.sleep(1)
    print('main')
    if not t.is_alive():
        break

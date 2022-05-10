import sys, threading

def run():
    print('thread start')
    time.sleep(1)
    print('thread stop')

th = threading.Thread(target=run)
print(th.is_alive())
th.start()
th.join()
print(th.is_alive())

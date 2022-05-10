import sys, threading

def run():
    while True:
        print('Thread {}'.format(threading.get_ident()))

print('Thread {}'.format(threading.get_ident()))

for i in range(5):
    my_thread = threading.Thread(target=run)
    my_thread.start()

print('Main thread exiting.')

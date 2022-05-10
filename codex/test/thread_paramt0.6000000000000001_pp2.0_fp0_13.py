import sys, threading
threading.Thread(target=lambda:
                sys.stdout.write('Hello from\nThread {}\n'.format(threading.get_ident()))
).start()

print('Hello from\nMain Thread {}'.format(threading.get_ident()))

print('ciao')

def show_value(data):
    try:
        val = data.value
    except ValueError:
        print('\nERROR:', str(data))
    else:
        print('\nYour value:', val)

def fetch_input(data):
    data.value = input('\nEnter value: ')

if __name__ == '__main__':
    mydata = Data()
    threading.Thread(target=show_value, args=(mydata,)).start()
    threading.Thread(target=fetch_input, args=(mydata,)).start()

import threading
from queue import Queue

def do_work(item):
    print('Processing:', item)

def worker():
    while True:
        item = q.get()
        do_work

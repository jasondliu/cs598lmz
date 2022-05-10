import threading
# Test threading daemon
from threading import Lock
from threading import Thread
import time
from random import randint
from random import random

from termcolor import colored
global lock
global number
global random_num
global stop_thread
lock = Lock()
stop_thread = False
random_num= 0
number = 0
def some_func(s):
    global number
    global random_num
    global stop_thread
    i = 0
    while stop_thread == False:
        if i == 500:
            break
        i+=1
        number = randint(0, 1000)
        random_num = randint(0, 1000)

        if random_num != number:
            print colored('Number: [%s] and Random Number: [%s]' % (number, random_num), 'red')
        else:
            print colored('Number: [%s] and Random Number: [%s]' % (number, random_num), 'green')

t = Thread(target=some_func, args=(5, ))
t.start()
time.sleep(1)
stop_thread = True

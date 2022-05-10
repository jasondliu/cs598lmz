import threading
# Test threading daemon

from time import sleep
from random import randint

def foo(tid):
    print('running in foo', tid)
    sleep(randint(1, 5))
    print('explicit context switch to foo')


def bar(tid):
    print('running in bar', tid)
    sleep(randint(1, 5))
    print('implicit context to bar')

if __name__ == '__main__':
    nloops = randint(2, 6)
    threads = []

    for i in range(nloops):
        t = threading.Thread(target=foo, args=(i,))
        threads.append(t)
        t.start()

    for i in range(nloops):
        t = threading.Thread(target=bar, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('all DONE')

# Reference web site
# https://docs.python.org/3/library/threading.html


# Both

import threading
threading.ThreadError

import time

from pymongo import MongoClient
client = MongoClient()
db = client.test

def f(n):
    #print(n)
    #time.sleep(0.1)
    return

def d():
    while True:
        print(threading.active_count())
        time.sleep(1)

def test():
    while True:
        db.test.insert({'a':'b'})
        time.sleep(0.1)

if __name__ == '__main__':
    #t = threading.Thread(target=d, args=())
    #t.start()
    #t.join()
    for i in range(4):
        t = threading.Thread(target=test, args=())
        t.start()
        time.sleep(0.1)

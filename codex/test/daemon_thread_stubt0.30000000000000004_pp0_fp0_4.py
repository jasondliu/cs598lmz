import sys, threading

def run():
    global counter, lock
    while True:
        lock.acquire()
        if counter < 10:
            counter += 1

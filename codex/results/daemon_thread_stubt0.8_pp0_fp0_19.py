import sys, threading

def run():
    print("thread B is started")
    print("thread B is being terminated")

print("thread A started")

thread = threading.Thread(target=run)
thread.start()

print("thread A terminated")

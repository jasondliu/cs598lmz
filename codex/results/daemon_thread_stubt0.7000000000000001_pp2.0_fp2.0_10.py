import sys, threading

def run():
    while True:
        print("Hello from thread")

print("Start thread")
thread = threading.Thread(target=run)
thread.start()

print("I'm back to main thread")

while True:
    print("Hello from main thread")

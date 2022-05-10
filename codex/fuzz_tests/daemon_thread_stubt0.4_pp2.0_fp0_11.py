import sys, threading

def run():
    for i in range(10):
        print(i)

threading.Thread(target=run).start()

print("Hello from main thread")

import sys, threading

def run():
    print("Hello from new thread")


t = threading.Thread(target=lambda: run())
t.start()

print("Hello from main thread")

sys.exit()

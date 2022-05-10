import sys, threading

def run():
    print("Thread started")
    while True:
        pass

thread = threading.Thread(target=run)
thread.start()

print("Thread running")
sys.exit()

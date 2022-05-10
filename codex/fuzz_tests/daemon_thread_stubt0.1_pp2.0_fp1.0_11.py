import sys, threading

def run():
    print("Thread started")
    for i in range(1, 100):
        print(i)
    print("Thread ended")

thread = threading.Thread(target=run)
thread.start()

print("Main thread")

# Thread started
# Main thread
# 1
# 2
# 3
# ...
# Thread ended

import sys, threading

def run():
    print("Thread started!")
    x = 0
    while True:
        x += 1

for i in range(10):
    my_thread = threading.Thread(target=run)
    my_thread.start()

print("Thread finished!")

import sys, threading

def run():
    global counter
    counter += 1
    print(counter)

counter = 0

for i in range(100):
    threading.Thread(target=run).start()

print(counter)

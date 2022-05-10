import sys, threading

def run():
    global count
    for i in range(1, 10000000):
        count += 1

count = 0
threading.Thread(target=run).start()
run()
print('count is ', count)

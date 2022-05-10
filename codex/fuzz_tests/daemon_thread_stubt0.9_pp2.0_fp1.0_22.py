import sys, threading

def run():
    for i in range(10):
        print(i)

t = threading.Thread(target=run)
t.daemon = False
t.start()

print('done')

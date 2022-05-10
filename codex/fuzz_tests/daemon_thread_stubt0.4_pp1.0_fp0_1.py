import sys, threading

def run():
    x = 0
    while True:
        x = x ^ 1

for i in range(4):
    threading.Thread(target=run).start()

while 1:
    pass

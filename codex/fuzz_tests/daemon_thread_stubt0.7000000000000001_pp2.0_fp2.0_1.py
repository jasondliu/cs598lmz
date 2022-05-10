import sys, threading

def run():
    global_var = threading.local()
    for i in range(1, 100):
        global_var.x = i
        print global_var.x

for i in range(1, 10):
    t = threading.Thread(target=run)
    t.start()

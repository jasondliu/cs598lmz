import sys, threading

def run():
    print('hi')
    sys.exit()

def run2():
    print('hi2')

def run3():
    print('hi3')

t = threading.Thread(target=run)
t2 = threading.Thread(target=run2)
t3 = threading.Thread(target=run3)
t.start()
t2.start()
t3.start()

# hi3
# hi2
# hi

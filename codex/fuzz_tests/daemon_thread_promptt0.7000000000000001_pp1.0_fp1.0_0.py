import threading
# Test threading daemon

def func1():
    print("Function 1 started")
    x = 0
    while True:
        time.sleep(1)
        x += 1
        print("F1: {}".format(x))

def func2():
    print("Function 2 started")
    x = 0
    while True:
        time.sleep(3)
        x += 1
        print("F2: {}".format(x))

t1 = threading.Thread(target=func1, args=())
t2 = threading.Thread(target=func2, args=())

t1.daemon = True
t2.daemon = True

t1.start()
t2.start()

time.sleep(10)
print("Finished")

# End test threading daemon

# Start test threading

#t1 = threading.Thread(target=func1, args=())
#t2 = threading.Thread(target=func2, args=())
#t1.start()
#t2.start()

#time.sleep(10)
#

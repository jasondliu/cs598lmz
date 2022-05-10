import threading
# Test threading daemon
def func():
    num = 0
    while True:
        num += 1
        if(num % 3 == 0):
            print("{} is mod 3.".format(num))
        time.sleep(1)
t1 = threading.Thread(target=func)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=func)
t2.daemon = True
t2.start()
print("End threading.")

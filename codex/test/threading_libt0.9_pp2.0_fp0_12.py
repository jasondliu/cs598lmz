import threading
threading.stack_size(500000)
############################################

now = datetime.datetime.now() 
start = now.strftime("%S")
print("Start counting...")
a = 0

def num1():
    a = 4
    time.sleep(2)
    a = a + 1
    print("This is %d from num1" % a)
    return a

def num2():
    a = 5
    time.sleep(1)
    a = a + 1
    print("This is %d from num2" % a)
    return a

def num3():
    a = 10
    a = a + 1
    print("This is %d from num3" % a)
    return a

def main():
    t1 = threading.Thread(target = num1, args = ())
    t2 = threading.Thread(target = num2, args = ())
    t3 = threading.Thread(target = num3, args = ())
    t1.start()
    t2.start()
    t3.start()


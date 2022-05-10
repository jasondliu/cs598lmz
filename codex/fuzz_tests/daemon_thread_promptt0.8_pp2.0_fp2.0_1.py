import threading
# Test threading daemon as we want our function calls to run in the background

def fun1():
    print("Fun1")
    time.sleep(3)
    print("Done Fun1")
    
def fun2():
    print("Fun2")
    time.sleep(4)
    print("Done Fun2")
    
    
# 1. Create a thread object by giving it a function object
t1 = threading.Thread(target = fun1)
t2 = threading.Thread(target = fun2)

t1.start()  # start() will execute the target function
t2.start()


# Print a message after completing all threads
print("Done")


# Note: Two threads running at a time.  After 3 seconds, t1 done and t2 is still running



# 2. Create a thread objects by overriding run() method
class MyThread(threading.Thread):
    def run(self):
        print("Thread Starting")
        time.sleep(5)
        print("Thread Ending")
        
t1 = MyThread()

t1.start()


# We can further override

import threading
# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-none

def test_daemon():
    print("start")
    time.sleep(2)
    print("end")

if __name__ == "__main__":
    t = threading.Thread(target=test_daemon)
    t.setDaemon(True)
    t.start()
    print("main thread")
    t.join()
    print("main thread end")

# Test threading lock
# https://www.geeksforgeeks.org/multithreading-python-set-1/

# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
import os 

def task1(): 
	print("Task 1 assigned to thread: {}".format(threading.current_thread().name)) 
	print("ID of process running task 1: {}".format(os.getpid())) 

def task2(): 
	print("Task 2 assigned to thread: {}

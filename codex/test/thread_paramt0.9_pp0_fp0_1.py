import sys, threading
threading.Thread(target=lambda: sys.stdout.write('yay!')).start()
 
# 更多信息，请参见threading.Thread

#=================================================================================================================
# 其他语言中常见的线程是用原子方法实现的。
import threading
import time

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0
shared_resource_with_rlock = 0
COUNT = 5000
shared_resource_lock = threading.Lock()
shared_resource_rlock = threading.RLock()

def increment_with_lock():
	global shared_resource_with_lock
	for i in range(COUNT):
		shared_resource_lock.acquire()
		shared_resource_with_lock += 1
		shared_resource_lock.release()

def decrement_with_lock():
	global shared_resource_with_lock

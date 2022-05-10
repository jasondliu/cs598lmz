import sys, threading

def run():
	while True:
		print("thread is running.")
		time.sleep(1)
	
if __name__ == '__main__':
	print("main thread is running. pid:%d" %os.getpid())
	# thread_test1 = threading.Thread(target=run(),args=())
	# thread_test1.setDaemon(True)	
	thread_test1 = threading.Thread(target=run,args=())
	thread_test1.setDaemon(True)	
	thread_test1.start()
	print("main thread end.")

# join() 等待
# daemon=True 后台线程

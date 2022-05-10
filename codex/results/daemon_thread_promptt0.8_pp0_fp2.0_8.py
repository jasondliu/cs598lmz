import threading
# Test threading daemon
def daemon_thread(thread_list,delay):
	count=0
	print(threading.current_thread().getName())
	while count<5:
		count+=1
		time.sleep(delay)
		#print(count)
		print('{} {}'.format(threading.current_thread().getName(),count))
	print('{} finished'.format(threading.current_thread().getName()))
	thread_list.remove(threading.current_thread())
	print(thread_list)
	#threading.current_thread().join()
	
if __name__=='__main__':
	thread_list=[]
	thread1=threading.Thread(target=daemon_thread,name='thread1',args=(thread_list,1))
	thread1.setDaemon(True)
	thread2=threading.Thread(target=daemon_thread,name='thread2',args=(thread_list,2))
	thread2.setDaemon(True)
	thread3=threading.Thread(target=daemon

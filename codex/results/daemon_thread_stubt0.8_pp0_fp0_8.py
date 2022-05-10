import sys, threading

def run():
	start = datetime.datetime.now()
	a = int(input('Enter lower limit of range:'))
	b = int(input('Enter upper limit of range:'))
	for i in range(a,b):
		print(i)
	end=datetime.datetime.now()
	print(end-start)

thread1 = threading.Thread(target=run)
thread2 = threading.Thread(target=run)
thread3 = threading.Thread(target=run)
thread4 = threading.Thread(target=run)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

import sys, threading

def run():
	global data
	data = []
	for i in range(20):
		print(threading.current_thread().name, i)
		data.append(i)

def run2():
	global data
	for i in range(20):
		print(threading.current_thread().name, i)
		data.append(i)

def run3():
	global data
	for i in range(20):
		print(threading.current_thread().name, i)
		data.append(i)

def run4():
	global data
	for i in range(20):
		print(threading.current_thread().name, i)
		data.append(i)

def run5():
	global data
	for i in range(20):
		print(threading.current_thread().name, i)
		data.append(i)

def run6():
	global data
	for i in range(20):
		print(threading.current_thread().name, i)
	

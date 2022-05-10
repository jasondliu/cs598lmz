import sys, threading

def run():
	def myfunc(e):
		print('Hello', end='')
		for i in range(1000000000): pass
		print('myfunc end')
	t = threading.Thread(target=myfunc, args=(1,))
	t.start()

def run_more():
	def myfunc(e):
		print('Hello', end='')
		for i in range(1000000000): pass
		print('myfunc end')
	t = threading.Thread(target=myfunc, args=(1,))
	t.start()

if __name__ == '__main__':
	run():
	run_more():

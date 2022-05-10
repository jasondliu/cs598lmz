import sys, threading

def run():
	x = 0
	while True:
		x = x + 1

for i in range(threading.activeCount()):
	print(i)
	t = threading.Thread(target=run)
	t.start()

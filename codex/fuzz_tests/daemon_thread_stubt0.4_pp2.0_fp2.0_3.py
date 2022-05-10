import sys, threading

def run():
	while True:
		print(1)
		time.sleep(1)

threading.Thread(target=run).start()

while True:
	print(2)
	time.sleep(1)

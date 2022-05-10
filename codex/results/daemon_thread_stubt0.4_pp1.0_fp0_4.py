import sys, threading

def run():
	for i in range(0, 10):
		print(i)
		time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
	print("Main")
	time.sleep(1)

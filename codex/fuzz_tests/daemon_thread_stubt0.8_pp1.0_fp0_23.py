import sys, threading

def run():
	print("run")
	while True:
		t = threading.Thread(target=timer)
		t.start()
		t.join()

def timer():
	time.sleep(2)
	sys.stdout.write(".")
	sys.stdout.flush()

run()

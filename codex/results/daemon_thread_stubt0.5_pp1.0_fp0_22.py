import sys, threading

def run():
	print("start")
	time.sleep(2)
	print("end")
	
print("start")
t = threading.Thread(target=run)
t.start()
print("end")

import sys, threading

def run():
	try:
		for i in range(10):
			print(i)
			time.sleep(1)	
	except:
		print("Error")
	else:
		print("Success")

t1 = threading.Thread(target=run)
t1.start()

t2 = threading.Thread(target=run)
t2.start()

t1.join()
t2.join()
sys.exit()

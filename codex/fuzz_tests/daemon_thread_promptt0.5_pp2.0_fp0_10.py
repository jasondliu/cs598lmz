import threading
# Test threading daemon

def func():
	print("func")
	
def run():
	print("run")
	
	t = threading.Thread(target=func)
	t.setDaemon(True)
	t.start()
	
	print("run end")
	
run()
print("main")

# Test threading daemon with sleep

def func():
	print("func")
	time.sleep(5)
	
def run():
	print("run")
	
	t = threading.Thread(target=func)
	t.setDaemon(True)
	t.start()
	
	print("run end")
	
run()
print("main")


# Test threading daemon with sleep

def func():
	print("func")
	time.sleep(5)
	
def run():
	print("run")
	
	t = threading.Thread(target=func)
	t.setDaemon(True)
	t.start()
	
	print("run end")
	
run()
print("main")

#

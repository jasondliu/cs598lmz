import sys, threading

def run():
	while True:
		with open("spike.out", "a+") as fp:
			fp.seek(0,2)
			if os.path.getsize("spike.out") >= 90*1024*1024:
				os.remove("spike.out")
			threading.current_thread().name
			fp.write(sys._getframe().f_code.co_name + ":%s\n" % threading.current_thread().name)
			fp.flush()
		time.sleep(0.3)

def run2():
	while True:
		with open("spike.out", "a+") as fp:
			fp.seek(0,2)
			if os.path.getsize("spike.out") >= 90*1024*1024:
				os.remove("spike.out")
			threading.current_thread().name
			fp.write(sys._getframe().f_code.co_name +

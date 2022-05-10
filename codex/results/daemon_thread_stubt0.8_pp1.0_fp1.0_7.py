import sys, threading

def run():
	print("running")
	if len(sys.argv) == 3:
		if sys.argv[2] == "0":
			obj_main.stop_all()
		else:
			obj_main.start_all()
	else:
		print("Provide one argument as '0' for stop or any other for restart")

def main():
	print("main")
	obj_main = Main.Main(sys.argv[1])
	t1 = threading.Thread(target=run)
	t1.start()
	t1.join()

main()

import sys, threading

def run():
	print(sys.argv[1])
	python_path = sys.argv[1]
	command = "python " + python_path + " ../../../match_results.json"
	print(command)
	os.system(command)

if __name__ == "__main__":
	print("Target:")
	print(sys.argv[0])
	
	python_path = ""
	sys.argv = sys.argv[1:]
	print(sys.argv)
	for arg in sys.argv:
		print(arg)
		python_path += arg + " "
	python_path = python_path[:-1]

	print(python_path)
	print("start")

	t1 = threading.Thread(target=run())
	t1.start()
	t1.join()
	t1 = threading.Thread(target=run())
	t1.start()
	t1.join()
	t1 = threading.Thread(target=run())
	t1.start()


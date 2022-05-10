import sys, threading

def run():
	file_path = os.path.dirname(sys.argv[0])
	file_path = "\\".join(file_path.split("\\")[:-1])
	sys.path.append(file_path)
	
	if getattr(sys, 'frozen', False):
		os.chdir(os.path.dirname(sys.executable))
	else:
		os.chdir(file_path)

	import main
	reload(main)
	main.main()


if __name__ == '__main__':
	if not (len(sys.argv) == 1):
		if sys.argv[1].lower() == 'open':
			import subprocess
			subprocess.run([sys.executable] + sys.argv[1:])
			exit()
		elif sys.argv[1].lower() == 'debug':
			import main
			reload(main)
			main.main()
		else:
			print('

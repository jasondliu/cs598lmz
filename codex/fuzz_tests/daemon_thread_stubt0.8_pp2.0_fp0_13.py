import sys, threading

def run():
	while True:
		output = command.stdout.readline()
		if output == '' and command.poll() is not None:
			break
		if output:
			print output.strip()

if __name__ == "__main__":
	filepath = sys.argv[1]
	print('reading {0}').format(filepath)

	with open(filepath) as f:
		commands = f.readlines()

	for c in commands:
		print c
		command = subprocess.Popen(c, stdout=subprocess.PIPE, shell=True)
		thread = threading.Thread(target=run)
		thread.start()
		thread.join()

import sys, threading

def run():
	f = open("sudo.txt")
	line = f.readline()
	while line:
		command = "sudo " + line
		os.system(command)
		line = f.readline()
	f.close()

sys.exit(run())

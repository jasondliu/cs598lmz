import sys, threading

def run():
	import os, sys
	CMD = " ".join(str(x) for x in sys.argv[1:])
	try:
		os.system(CMD)
	except:
		pass

def main(file="", mode="", verbose=False, *args):
	if file:
		print "Running", file
		threading.Thread(target=run, args=(file,)).start()
	else:
		print "No file to run."

if __name__ == "__main__":
	main(*sys.argv)

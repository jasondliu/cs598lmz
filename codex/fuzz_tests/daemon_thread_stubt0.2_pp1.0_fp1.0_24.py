import sys, threading

def run():
	print("run")
	sys.exit()

threading.Thread(target=run).start()

print("main")

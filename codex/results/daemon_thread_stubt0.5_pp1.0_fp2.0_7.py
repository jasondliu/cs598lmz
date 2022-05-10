import sys, threading

def run():
	while True:
		command = input(">>> ")
		if command == "quit":
			sys.exit(0)
		else:
			print("Unknown command:", command)

threading.Thread(target=run).start()

import time

while True:
	print("Hello!")
	time.sleep(1)

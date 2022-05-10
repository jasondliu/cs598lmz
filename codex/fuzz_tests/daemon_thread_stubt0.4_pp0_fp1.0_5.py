import sys, threading

def run():
	print("Hello from new thread")
	return

t = threading.Thread(target=run)
t.start()

print("Hello from main thread")

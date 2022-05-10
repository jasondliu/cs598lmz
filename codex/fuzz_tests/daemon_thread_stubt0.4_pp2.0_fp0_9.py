import sys, threading

def run():
	print("Hello from new thread")

thread = threading.Thread(target=run)
thread.start()

print("Hello from main thread")

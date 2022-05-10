import sys, threading

def run():
	time.sleep(0.01)
	print(2)

thread = threading.Thread(target=run)
thread.start()

if __name__ == "__main__":
	time.sleep(0.02)
	print(1)

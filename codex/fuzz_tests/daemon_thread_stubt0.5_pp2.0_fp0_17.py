import sys, threading

def run():
	os.system("python3.6 main.py")

def main():
	global thread
	thread = threading.Thread(target=run)
	thread.start()

if __name__ == "__main__":
	main()

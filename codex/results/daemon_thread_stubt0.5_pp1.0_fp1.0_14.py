import sys, threading

def run():
	while True:
		print("Threading")
		time.sleep(0.5)

def main():
	th = threading.Thread(target=run)
	th.start()
	while True:
		print("Main")
		time.sleep(0.5)

if __name__ == "__main__":
	main()

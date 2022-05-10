import sys, threading

def run():
	while True:
		for i in range(0, 100):
			print(i)
			time.sleep(1)

def main():
	t = threading.Thread(target=run)
	t.start()
	while True:
		print("main")
		time.sleep(1)

if __name__ == "__main__":
	main()

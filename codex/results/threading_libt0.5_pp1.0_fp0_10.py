import threading
threading.stack_size(67108864)

def run():
	while True:
		#print("Hello")
		a = 1 + 1
		#time.sleep(1)


def main():
	for i in range(1):
		t = threading.Thread(target=run)
		t.start()

if __name__ == "__main__":
	main()

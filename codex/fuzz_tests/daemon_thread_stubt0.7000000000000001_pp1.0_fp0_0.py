import sys, threading

def run():
	for i in range(1, 11):
		print('\t' + str(i))

if __name__ == '__main__':
	if len(sys.argv) == 2:
		count = int(sys.argv[1])
	else:
		count = 10

	threads = []
	for i in range(count):
		threads.append(threading.Thread(target=run, args=()))

	for t in threads:
		t.start()
	for t in threads:
		t.join()

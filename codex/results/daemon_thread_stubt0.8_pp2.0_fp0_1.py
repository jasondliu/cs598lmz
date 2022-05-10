import sys, threading

def run():
	print("Start")
	while(1):
		x=1

def main():
	threads=[]
	for i in range(100):
		t=threading.Thread(target=run)
		threads.append(t)
		t.setDaemon(True)
		t.start()

	for t in threading.enumerate():
		print(t.name)
	print("Done")

if __name__ == "__main__":
	main()

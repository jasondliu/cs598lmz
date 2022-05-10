import sys, threading

def run():
	t = threading.current_thread()
	while True:
		print "Thread %s is running" % t.name
		sys.stdout.flush()
		time.sleep(1)

def main():
	t = threading.Thread(target=run, name="DemoThread")
	t.start()
	t.join(5)
	print "Thread %s is ended" % t.name

if __name__ == "__main__":
	main()

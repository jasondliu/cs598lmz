import sys, threading

def run():
	while True:
		sys.stdout.write("\r%s" % datetime.datetime.now())
		sys.stdout.flush()
		time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
	try:
		sys.stdout.write("\r%s" % raw_input(""))
		sys.stdout.flush()
	except:
		break

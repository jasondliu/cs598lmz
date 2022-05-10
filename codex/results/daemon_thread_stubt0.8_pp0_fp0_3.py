import sys, threading

def run():
	while 1:
		hd.p.put("MSG_FROM_CLIENT")
		time.sleep(0.5)
	
if __name__ == "__main__":
	c = client("127.0.0.1", 8000)
	t = threading.Thread(target=run)
	t.daemon = True
	t.start()
	
	while 1:
		msg = c.get()
		if msg:
			print msg
		time.sleep(0.1)

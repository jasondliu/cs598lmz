import sys, threading

def run():
	while True:
		time.sleep(0.5)
		print(threading.current_thread().ident)

t = threading.Thread(target=run)
t.start()

#sys.exit()

#print(threading.current_thread().ident)

#t.join()

print('end')

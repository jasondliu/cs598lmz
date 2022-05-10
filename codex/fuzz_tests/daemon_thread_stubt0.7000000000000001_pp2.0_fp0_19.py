import sys, threading

def run():
	sys.stdout.write('.')
	sys.stdout.flush()

threads = []
for i in range(100):
	threads.append(threading.Thread(target=run))
	threads[-1].start()

for i in range(100):
	threads[i].join()

print('\nDone')

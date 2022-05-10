import sys, threading

def run():
	if len(sys.argv) == 1:
		print "No input file specified."
		return
	inFile = open(sys.argv[1])
	outFile = open(sys.argv[2], 'w') if len(sys.argv) > 2 else sys.stdout
	
	for line in inFile:
		words = line.split()
		for i in range(len(words)):
			if words[i].startswith('@'):
				words[i] = '@' + words[i][1:].lower()
		outFile.write(' '.join(words) + '\n')

threads = []
for i in range(5):
	threads.append(threading.Thread(target=run))
	threads[-1].start()

for i in range(5):
	threads[i].join()

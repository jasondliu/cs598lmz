import sys, threading

def run():
	global fileCount
	global files
	global blockSize
	global offset
	global progress
	global fileSize
	global fileName
	global threadCount
	global printLock
	blockCount = int(fileSize / blockSize)
	if fileSize % blockSize > 0:
		blockCount += 1
	for i in range(0, blockCount):
		offset = i * blockSize
		file = open(fileName, 'rb')
		file.seek(offset)
		block = file.read(blockSize)
		file.close()
		hash = hashlib.sha256(block).hexdigest()
		printLock.acquire()
		print('Thread ' + str(threading.current_thread().ident) + ': ' + hash)
		progress += 1
		printLock.release()

def printProgress():
	global progress
	global fileCount
	global printLock
	while progress < fileCount:
		printLock.acquire()
		sys.stdout.write('\rCompleted ' + str(progress

import sys, threading

def run():
	t = threading.Thread(target=parseLogs)
	t.start()

def parseLogs():
	logPath = "logs/"
	logFiles = os.listdir(logPath)
	for file in logFiles:
		f = open(logPath + file,'r')
		lines = f.readlines()
		for line in lines:
			parseLine(line)
		f.close()

def parseLine(line):
	try:
		items = line.split('|')
		if len(items) != 3:
			return
		if items[1].find("content") > -1:
			parseContent(items[1])
		elif items[1].find("play") > -1:
			parsePlay(items[1])
		elif items[1].find("watched") > -1:
			parseWatched(items[1])
	except Exception, e:
		print("error: " + str(e))
		traceback.

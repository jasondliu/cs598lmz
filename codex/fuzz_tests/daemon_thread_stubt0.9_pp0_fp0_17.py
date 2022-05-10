import sys, threading

def run():
	collection = {}
	COLLECTION_FILE = open("logs.txt", "r")
	sys.stderr.write("reading file \n")
	for line in COLLECTION_FILE:
		(key,val) = line.strip().split("\t")
		if key in collection:
			collection[key] = collection[key] + "\n" + val
		else:
			collection[key] = val
	sys.stderr.write("reading file complete \n")
	COLLECTION_FILE.close()

	sys.stderr.write("writing new collection \n")
	COLLECTION_FILE = open("logs_new.txt", "w")
	for key in collection.keys():
		COLLECTION_FILE.write("%s\t%s\n" %(key,collection[key]))
	sys.stderr.write("writing complete \n")
	COLLECTION_FILE.close()

#threading.Thread(target=run).start()	
run()

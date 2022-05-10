import sys, threading

def run():
	#first we're going to launch a client and server.
	subprocess.Popen(['python', 'server.py'])
	subprocess.Popen(['python', 'client.py'])
	subprocess.Popen(['python', 'client.py'])
	subprocess.Popen(['python', 'client.py'])

	#wait for the first client to be done (i.e. the first client we connected to lives for long enough)
	input('press enter to teardown server')
	
	#now we're going to launch a client and a server
	subprocess.Popen(['python', 'server.py'])
	subprocess.Popen(['python', 'client.py'])
	subprocess.Popen(['python', 'client.py'])

if __name__ == '__main__':
	run()

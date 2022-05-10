import sys, threading

def run():
	#run server
	threading.Thread( target=server.run, args=(), kwargs={} ).start()
	#wait
	time.sleep(1)
	#start bot
	if len(sys.argv) > 1:
		if sys.argv[1] == 'bot':
			bot.run()
	#run client
	threading.Thread( target=client.run, args=(), kwargs={} ).start()

if __name__ == '__main__':
	run()

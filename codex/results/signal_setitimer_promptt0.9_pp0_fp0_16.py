import signal
# Test signal.setitimer for 1 automata

import signal
#
#	Test signal.setitimer 
#

def signal_handler(signal,frame):
	print "signal_handler"
	global TOKEN
	global TIMER
	if signal == signal.SIGALRM:
		print "Timer expires"
		TIMER -=1
		if (TIMER ==0):
			TOKEN += 1
			if TOKEN > 4:
				TOKEN =0
			TIMER = 5
	
signal.signal(signal.SIGALRM,signal_handler)



def alternant1 ():
	print "alternant1"
	signal.setitimer(signal.ITIMER_REAL,0,1)  # Expiry every second (1,0->start immediatly)
	while(True):
		pass	



TIMER = 5
TOKEN = 0


alternant1()

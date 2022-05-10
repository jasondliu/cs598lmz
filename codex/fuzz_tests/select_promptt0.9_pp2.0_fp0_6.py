import select
# Test select.select() the manual way
#
# Plug in the code below and read() from stdin in the current shell to see what happens
#
# I recommend usnig ipython if you want to test it because it can help you with formatting
#
# Also, you could use telnet localhost 3000 and hit enter lots
# of times to test it

import select
from time import time

print "Type in lots of stuff into stdin of this script and hit Ctrl+D"
print "Or use the telnet command from another terminal so you can read what is going on"

period_secs = .5
incoming = []
last_checked = time()

while True:
	if time() - last_checked > .5:
		# The poll period for this example
		
		# This is where you put anything you have to do at every interval
		# The stuff below is just so you can see what happens when you input into this
		# terminal
		print "poll period elapsed"
		print "incoming is {}".format(incoming)
		incoming = []
		

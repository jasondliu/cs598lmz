import threading
# Test threading daemon
# Importing
import threading

# Two threads calling the same function

def hello_world(delay):
	'''
	Function to print Hello World.
	Params
	------
		delay: delay before printing.
	'''
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print("Hello World!")

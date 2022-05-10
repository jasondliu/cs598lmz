import sys, threading

def run():
	global thread
	thread = threading.Thread(target=run)
	thread.daemon = True
	thread.start()
	
def stop():
	global thread
	thread.stop()

def get_input(timeout=0.1):
	listener = keyboard.Listener(on_press=on_press)
	listener.start()
	
	listener.join()
	
def on_press(key):
	try:
		print('alphanumeric key {0} pressed'.format(key.char))
	except AttributeError:
		print('special key {0} pressed'.format(key))
	
	if key == keyboard.Key.esc:
		# Stop listener
		return False
	
if __name__ == "__main__":
	run()

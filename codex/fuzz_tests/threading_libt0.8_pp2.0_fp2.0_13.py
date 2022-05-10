import threading
threading.stack_size(1024*1024*16)

def timed_callback(f, args, seconds):
	event = threading.Event()
	def timer_thread():
		event.wait(seconds)
		if not event.isSet():
			f(*args)
	t = threading.Thread(target=timer_thread)
	t.start()

def free_resources(resources):
	for item in resources:
		item.close()

def _get_week():
	today = datetime.datetime.now()
	return today.isocalendar()[1]

def get_current_week():
	"""
	Return the current week number in the year.
	"""
	return _get_week()

def get_next_week():
	"""
	Take the current week and add one.
	Easily modified to take an offset if needed.
	"""
	return _get_week() + 1

def extract_intervals(time_list):
	"""
	Parse time list into open intervals.
	"""
	

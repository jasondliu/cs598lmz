import sys, threading

def run():
	global max_value, can_get_max
	while 1:
		if not can_get_max:
			break
		elif max_value == 100:
			can_get_max = False
		else:
			max_value = 100
		time.sleep(0.01)
	
def main():
	t=thr

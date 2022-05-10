import sys, threading

def run():
	while True:
		cmd = sys.stdin.readline()
		if cmd == '\n':
			continue
		print('>>', cmd, '<<')
		if cmd:
			if cmd[0] == '\n':
				break
			if cmd[0] == '0' or cmd[0] == '1':
				# gc.collect(2)
				gc.collect(1)
				gc.collect(0)
#				print(gc.get_count())
				print(gc.get_count(), len(gc.get_objects()))
#				m = gc.get_referrers(*gc.get_objects())
#				print(len(m), m)
#				m = gc.get_referrers(m)
#				print(len(m), m)
#				m = gc.get_referrers(m)
#	

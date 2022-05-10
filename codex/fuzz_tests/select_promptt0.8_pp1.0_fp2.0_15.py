import select
# Test select.select

print('Entering main loop')
while True:
	print('waiting for the next event')
	# wait for at most 30 seconds for the next event
	ready = select.select([sys.stdin], [], [], 30)
	if ready[0]:
		# read from stdin and print
		print('Read stdin:', sys.stdin.readline(), end='')
	else:
		print('Doing other work')

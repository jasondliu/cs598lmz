import select
# Test select.select()

print 'start'

timeout = 0
for i in xrange(1, 10):
	readable, writeable, exceptional = select.select([], [], [], timeout)

	if readable:
		print '\nreadable:'
		for h in readable:
			print h

	if writeable:
		print '\nwriteable:'
		for h in writeable:
			print h

	if exceptional:
		print '\nexceptional:'
		for h in exceptional:
			print h

	print '\n'

print 'end'

# Test select.poll()

print 'start'

poller = select.poll()
for i in xrange(1, 10):
	events = poller.poll(timeout)

	for file, event in events:
		print 'file = {}, event = {}'.format(file, event)
		
	print '\n'

print 'end'

# Test select.epoll()

print 'start'

epoller = select.

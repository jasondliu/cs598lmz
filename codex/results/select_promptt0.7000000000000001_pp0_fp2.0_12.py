import select
# Test select.select
# Returns three lists of objects ready for reading, writing, or
# exceptional processing.
# For example:
#	read, write, exception = select.select(read_list, write_list, [], 1.0)

# For convenience, in the next two functions, we assume that there are
# two files in read_list: the socket and a file (a pipe) from which
# we've read a '\n'-terminated line.

def server(read_list, write_list, error_list):
	for f in read_list:
		if f is sock:
			message, addr = f.recvfrom(MAX_SIZE)
			print 'Got message from:', addr
			print 'Message reads:', message
			# We don't expect any writes, but ...
			if f in write_list:
				f.sendto('Your data was %d bytes' % len(message), addr)
		else:
			line = f.readline()
			print 'The command line reads:', line

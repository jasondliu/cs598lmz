import socket
# Test socket.if_indextoname()
#
# Usage: if_index

try:
	import sockeye.test_util
except ImportError:
	print 'Cannot import sockeye.test_util'
	print 'This program must be run from the test/ subdirectory'
	import sys
	sys.exit(1)

import sockeye.test_util

# Print usage
def usage():
	print 'Usage: %s if_index' % sys.argv[0]

# Start of main program
if len(sys.argv) != 2:
	usage()
	sys.exit(1)

# First argument is the interface index
try:
	index = int(sys.argv[1])
except:
	print 'Invalid interface index: %s' % sys.argv[1]
	usage()
	sys.exit(1)

print 'Testing socket.if_indextoname(%u)...' % index
name = socket.if_indextoname(index)
print 'Returned name: "%s"' % name
sockeye.test_util.check_

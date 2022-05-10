import socket
# Test socket.if_indextoname
# socket.getifaddrs()

import urlparse
# urlparse.urlparse(url_string)
# urlparse.urlunparse(parsed_url)
# Parsed Result: [0] = scheme
#                [1] = netloc
#                [2] = path
#                [3] = params
#                [4] = query
#                [5] = fragment
#                [6] = username
#                [7] = password
#                [8] = hostname
#                [9] = port

import uuid
# uuid.getnode()
# uuid.getnode() returns the MAC address
# of the first ethernet interface found

import sys
if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'Usage: %s <mac-addrs-file>' % sys.argv[0]
		sys.exit(1)
	print '=' * 80
	print '=' * 80
	print '=' * 80
	print 'Running on Host: %s (%

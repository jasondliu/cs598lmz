import socket
# Test socket.if_indextoname()
if_indextoname(11, None)
if_indextoname(11, 'abc')

if_indextoname(11, 'abcde')
if_indextoname(11, 'abcdefg')
if_indextoname(11, 'abcdefgh')
if_indextoname(11, 'abcdefghi')
if_indextoname(11, 'abcdefghij')

if_indextoname(11)
if_indextoname(11, '')
if_indextoname(11, b'')

if_indextoname(11, 'abcde', 1)
if_indextoname(11, 'abcdefg', 2)
if_indextoname(11, 'abcdefgh', 3)
if_indextoname(11, 'abcdefghi', 4)
if_indextoname(11, 'abcdefghij', 5)

# Test socket.gethostbyname()
gethostbyname('localhost')
gethostbyname('')
get

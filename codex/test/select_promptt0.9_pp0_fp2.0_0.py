import select
# Test select.select
#
from System.Diagnostics import Stopwatch
watch = Stopwatch()
import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setblocking(0)
soc.bind(('0.0.0.0', 80))
soc.listen(5)

# One million times
loop = 10000000

#print 'waiting to accept() %d times' % loop
#select.select([soc], [], [], 0.1)

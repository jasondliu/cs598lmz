import select
# Test select.select() using stdin
import sys, time
input = [sys.stdin]
output = []
timeout = 10

print 'starting'
start_time = time.time()
input_ready,output_ready,except_ready = select.select(input, output, input, timeout)
if input_ready == []:
	print 'Time is up.'
else:
	print 'Recieved input after %s seconds' % (time.time() - start_time)

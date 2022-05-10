import select
# Test select.select()
(rList, wList, xList) = select.select([sys.stdin], [], [], 5)
for fd in rList:
    s = fd.readline()
    print 'Read', s

print 'with stdin polling'
import sys
import select
# Test select.poll()
p = select.poll()
p.register(sys.stdin, select.POLLIN)
while True:
    if p.poll(10000): # poll in 10 seconds
        s = sys.stdin.readline()
        print 'Read', s
    else:
        print 'No input'

print 'with stdin piping'
import sys
import time
# Test pipe-based IPC
stdin, stdout = os.pipe()
read, write = os.fdopen(stdin, 'r', 0), os.fdopen(stdout, 'w', 0)
print >> write, 'starting'
write.close()
select.select([read], [], []) # wait for read to be ready
s = read.readline()
print 'Read',

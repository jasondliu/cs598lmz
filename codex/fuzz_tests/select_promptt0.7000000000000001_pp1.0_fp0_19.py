import select
# Test select.select

rs, ws, xs = select.select([], [], [], 3)
print '%d, %d, %d' % (len(rs), len(ws), len(xs))
# Test select.poll

p = select.poll()
p.register(sys.stdin, select.POLLIN)

while True:
    events = p.poll()
    for fd, event in events:
        if fd == sys.stdin.fileno():
            print "Got input", sys.stdin.readline()
        else:
            print "Got unknown event"
# Find files in a directory hierarchy

import os
import fnmatch

for root, dirnames, filenames in os.walk('/tmp/'):
    for filename in fnmatch.filter(filenames, '*.py'):
        print os.path.join(root, filename)
# Test smtplib

import smtplib

s = smtplib.SMTP('localhost')
s.sendmail('noreply@example.com', 'user@

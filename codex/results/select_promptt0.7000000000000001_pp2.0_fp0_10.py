import select
# Test select.select

print 'Before select...'
rfds, wfds, efds = select.select([sys.stdin], [], [], 5)
print 'After select...'

#rfds: ready-to-read file descriptors;
#wfds: ready-to-write file descriptors;
#efds: error file descriptors;
#select return 3 subset of input file descriptors;

for f in rfds:
    print 'select return: %s' % f.readline()
    
# select will block until the file descriptor(fd) is ready, or the timeout;

# select return 3 subset of input file descriptors:
# 1.rfds: ready-to-read file descriptors;
# 2.wfds: ready-to-write file descriptors;
# 3.efds: error file descriptors;

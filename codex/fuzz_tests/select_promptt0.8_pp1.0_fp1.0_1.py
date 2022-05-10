import select
# Test select.select function
print('Starting')

rlist, wlist, xlist = select.select([sys.stdin], [], [], 0.1)
print('rlist', rlist)
print('wlist', wlist)
print('xlist', xlist)

if rlist:
    s = sys.stdin.readline()
    print('-> Got:', s)
else:
    print('Nothing')
print('Done')

# Test select.poll function
print('Starting')
p = select.poll()
p.register(sys.stdin.fileno(), select.POLLIN)

while True:
    evts = p.poll(1000)  # timeout in ms
    print('evts', evts)
    for fd, flag in evts:
        s = sys.stdin.readline()
        print('-> Got:', s)

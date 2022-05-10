import select
# Test select.select
print('Testing select()...')

# get a list of pipes
reader, writer = os.pipe()
rlist = [reader]
wlist = [writer]

# figure out if select() will block
timeout = 0.2
rl, wl, xl = select.select(rlist, wlist, rlist, timeout)
if rl:
    print('Ready to read;', len(rl), 'selections:', rl)
if wl:
    print('Ready to write;', len(wl), 'selections:', wl)

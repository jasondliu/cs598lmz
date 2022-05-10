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
if xl:
    print('Exceptional condition on', len(rl), 'selections:', xl)
else:
    print('No exceptional conditions on any of', len(rl)+len(wl), 'selections')

print('Calling select() again')
rl, wl, xl = select.select(rlist, wlist, rlist, timeout)
if rl:
    print('Ready to read;', len(rl), 'selections:', rl)
if wl:
    print('Ready to write;

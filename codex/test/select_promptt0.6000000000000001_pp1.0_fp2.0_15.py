import select
# Test select.select
r, w, x = select.select([], [], [], 0)
print('r =', r)
print('w =', w)
print('x =', x)

# Test select.poll
p = select.poll()
p.register(sys.stdin)

while True:
    events = p.poll(1000)
    print('events =', events)
    if events:
        print('Reading')
        line = sys.stdin.readline()

import select
# Test select.select()
inputs = [sys.stdin]
outputs = []
readable, writable, exceptional = select.select(inputs, outputs, inputs)
print('inputs:', inputs)
print('readable:', readable)
print('writable:', writable)
print('exceptional:', exceptional)

# Test select.poll()
p = select.poll()
p.register(sys.stdin)
events = p.poll()
print('events:', events)

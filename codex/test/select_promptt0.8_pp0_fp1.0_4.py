import select
# Test select.select()
# https://docs.python.org/3/library/select.html#select.select
print('start')
inputs = [sys.stdin]
outputs = []
readable, writable, exceptional = select.select(inputs, outputs, inputs, 10)
print('readable = %s' % readable)
print('writable = %s' % writable)
print('exceptional = %s' % exceptional)
print('finish')

# Also, can use select.poll()

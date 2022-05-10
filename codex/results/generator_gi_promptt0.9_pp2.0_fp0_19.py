gi = (i for i in ())
# Test gi.gi_code is None.
print(gi.gi_code)
# Would cause an exception because gi_frame
# is also None.
print(gi.gi_frame)

# A more interesting example.
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

# Create the generator.
c = countdown(3)
# Can't print it directly.
# print(c)

# Send in a value.
print(c.send(None))
# Send in a value.
print(c.send(None))
# Send in a value.
print(c.send(None))
# We're done!
print(c.send(None))
print(c.send(None))
# Would cause an exception.
# print(c.send(None))

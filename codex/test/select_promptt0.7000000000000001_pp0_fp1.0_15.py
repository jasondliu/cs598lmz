import select
# Test select.select()

inputs = [open("/dev/tty"), open("/dev/tty"), open("/dev/tty")]

print("Calling select()")
readable, writeable, exceptional = select.select(inputs, [], [])

print("select() returned %d" % len(readable))
print("readable:", readable)
print("writeable:", writeable)
print("exceptional:", exceptional)

print("Readable file descriptors:")
for stream in readable:
    print(stream)

print("Writeable file descriptors:")
for stream in writeable:
    print(stream)

print("Exceptional file descriptors:")
for stream in exceptional:
    print(stream)

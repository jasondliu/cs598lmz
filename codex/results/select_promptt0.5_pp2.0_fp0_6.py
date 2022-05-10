import select
# Test select.select()

# Create some pipes
r, w = os.pipe()

# Make the read end non-blocking
fl = fcntl.fcntl(r, fcntl.F_GETFL)
fcntl.fcntl(r, fcntl.F_SETFL, fl | os.O_NONBLOCK)

# Write some data
os.write(w, "Hello")

# Wait for the data to be read
while True:
    rl, wl, xl = select.select([r], [], [], 1)
    if not rl:
        print "No data"
        continue
    print "Readable:", rl
    print "Data:", os.read(r, 1024)
    break
</code>


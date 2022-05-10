from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'n'
s.size = calcsize(s.format)

# Parse the stream into a list of (ts, data) tuples
stream = []
while True:
    try:
        d = f.read(s.size)
        ts, = s.unpack(d)
        stream.append(ts)
    except Exception:
        break

a = np.array(stream)

# Check for timestamp overflow and correct it
if a[-1] < a[0]:
    a += 1 << 16

# Convert to microseconds
a *= 1e6 / 256.0

# Take the difference to get the delay between packets
a = np.diff(a)

# Plot the delay as a histogram
plt.hist(a, bins=np.logspace(-3, 0, num=20))
plt.gca().set_xscale('log')
plt.show()

# Calculate the average and 99th percentile
avg = a.mean()
p99 = np.percentile(a, 99)


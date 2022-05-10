import socket
# Test socket.if_indextoname for performance
#
# Results: I would not worry about calling it often. It takes 0.00012 seconds
# to find the name for an interface where the interface index is known
#
# It takes between 0.06 and 0.5 seconds to look up the other direction, i.e.
# to go from name to index. It does seem to be significantly affected by the
# type of interface (does it have an ipv4 / ipv6 address or not?).

# Get the name for a given index
num_samples = 1000
names = []
times = []
for _ in range(num_samples):
    start = time.time()
    names.append(socket.if_indextoname(3))
    times.append(time.time() - start)
s = pd.Series(times, names=["clock"])
print(s)
print(s.describe())
# Get the index for all available interfaces
num_samples = 100
names = []
times = []
for _ in range(num_samples):
    start = time.time()
    names.append

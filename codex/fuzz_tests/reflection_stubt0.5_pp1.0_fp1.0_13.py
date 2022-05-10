fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# with open('/etc/passwd') as f:
#     print(f.read())

# with open('/etc/passwd') as f:
#     print(f.read().splitlines())

# with open('/etc/passwd') as f:
#     print(f.readline())

# with open('/etc/passwd') as f:
#     print(f.readlines())

# with open('/etc/passwd') as f:
#     for l in f:
#         print(l)

# with open('/etc/passwd') as f:
#     print(f.read(5))

# with open('/etc/passwd') as f:
#     print(f.read(5))
#     print(f.read(5))

# with open('/etc/passwd') as f:
#     print(f.read(5))
#     print(f.read())

# with open('/etc/passwd') as f:
#     print(f

import select
# Test select.select()
# https://docs.python.org/3/library/select.html
# https://realpython.com/python-sockets/#the-basic-socket-client

# Use python3 select-test.py for all tests

# Test 1
# First test with no data
print("Test 1")
for i in range(5):
    (i, o, e) = select.select([], [], [], 1)
    print(i, o, e)

# Test 2
# Add data to stdin
print("Test 2")
sys.stdin.write("hi\n")
sys.stdin.flush()
for i in range(5):
    (i, o, e) = select.select([sys.stdin], [], [], 1)
    print(i, o, e)

# Test 3
# Add data to client socket
print("Test 3")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 31337))

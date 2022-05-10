import select
# Test select.select

def test(readable):
    print("Testing", readable)
    readable, writable, exceptional = select.select(readable, [], [], 1)
    print("  readable:", readable)
    print("  writable:", writable)
    print("  exceptional:", exceptional)

# Test a set of readable objects: stdin, a socket, and a file

print("-- Testing a set of readable objects: stdin, a socket, and a file")
test( [sys.stdin, socket.socket(socket.AF_INET, socket.SOCK_STREAM), open("/etc/passwd")] )

# Test a set of writable objects: stdout and a socket

print("-- Testing a set of writable objects: stdout and a socket")
test( [sys.stdout, socket.socket(socket.AF_INET, socket.SOCK_STREAM)] )

# Test a set of exceptional objects: stdin and a socket

print("-- Testing a set of exceptional objects: stdin and a socket")
test( [sys.stdin, socket.

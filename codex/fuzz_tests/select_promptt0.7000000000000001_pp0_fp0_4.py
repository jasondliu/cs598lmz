import select
# Test select.select

while True:
    readable, _, _ = select.select([sys.stdin], [], [], 1)
    if readable:
        print("Input ready")
        data = sys.stdin.readline()
        print("Data received: {}".format(data))
    else:
        print("No input")

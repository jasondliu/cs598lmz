import select
# Test select.select()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 0))
s.listen(4)

read, write, err = select.select([s], [], [], 1)
if (read != [s]):
    print("Bad result from select.select().\n")

read, write, err = select.select([],[], [s], 1)
if (err != [s]):
    print("Bad result from select.select().\n")

read, write, err = select.select([], [s], [], 1)
if (write != [s]):
    print("Bad result from select.select().\n")

read, write, err = select.select([s], [s], [s], 1)

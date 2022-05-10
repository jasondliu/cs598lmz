import select
# Test select.select
reader, writer, err = select.select([], [], [], 0)
print(reader, writer, err)

# Test select.poll
p = select.poll()
p.register(sys.stdin, select.POLLIN)
while 1:
    poll_result = p.poll(100)
    print(poll_result)
    if poll_result:
        print(sys.stdin.readline())

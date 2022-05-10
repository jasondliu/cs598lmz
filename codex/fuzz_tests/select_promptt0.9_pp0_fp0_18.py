import select
# Test select.select()

poll = select.poll()

poll.register(sys.stdin)

inputs = {}

while True:
    print('poll')
    result = poll.poll(1) # 1 second
    print('poll result:', result)
    if result:
        for fd, events in result:
            buf = os.read(fd, 1000)
            print('read', fd, events, buf)
            if not buf:
                break
            inputs[fd].append(buf)
    else:
        print('wait...')

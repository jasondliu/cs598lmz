import select
# Test select.select()
timeout = 5
readable, writable, exceptional = select.select([sys.stdin], [], [], timeout)
if readable:
    print("stdin is ready!")
else:
    print("Timed out!")

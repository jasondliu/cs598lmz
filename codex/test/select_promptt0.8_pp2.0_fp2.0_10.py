import select
# Test select.select()
read, write, error = select.select([sys.stdin], [], [], 1)

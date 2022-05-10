import select
# Test select.select()

while True:
    s = select.select([sys.stdin], [], [], 10)

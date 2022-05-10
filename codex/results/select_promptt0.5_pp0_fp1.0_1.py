import select
# Test select.select()

#select.select([sys.stdin], [], [])
#select.select([sys.stdin], [], [], 0)

select.select([sys.stdin], [], [], 1)

#select.select([], [sys.stdout], [])
#select.select([], [sys.stdout], [], 0)

#select.select([], [sys.stdout], [], 1)

import select
# Test select.select
# https://docs.python.org/2/library/select.html#select.select

rfds, wfds, xfds = select.select([sys.stdin], [], [])

if not rfds:
    print("Cannot select")


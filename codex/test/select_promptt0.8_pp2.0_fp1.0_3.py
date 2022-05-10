import select
# Test select.select() by selecting only stdin.
[i,o,e] = select.select([sys.stdin],[],[],0.0)
# If input is waiting, read it.

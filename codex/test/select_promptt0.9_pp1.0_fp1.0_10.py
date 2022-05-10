import select
# Test select.select()
(rList, wList, xList) = select.select([sys.stdin], [], [], 5)

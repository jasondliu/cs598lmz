import select
# Test select.select with standard input open
#
select.select([0], [], [])

# Test select.select with specific timeout
#
select.select([], [], [], 0.001)

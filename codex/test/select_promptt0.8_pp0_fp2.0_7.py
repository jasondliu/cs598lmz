import select
# Test select.select to see if it works as expected.

x = range(5)
print(select.select(x, [], [], 3))

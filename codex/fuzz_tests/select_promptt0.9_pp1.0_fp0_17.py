import select
# Test select.select
r, w, x = select.select ([], [1], [])
assert not r
assert w == [1]
assert not x

r, w, x = select.select ([1, 2], [3, 4], [5, 6])
assert r == [1, 2]
assert w == [3, 4]
assert x == [5, 6]

r, w, x = select.select ([1, 2], [], [])
assert r == [1, 2]
assert not w
assert not x

# +2 for the two ttys stdin/stdout use
assert len(select.select ([1, 2], [], [], 0)) == 2 + 2

select.select ([], [], [], 0)  # should not crash

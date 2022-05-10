import select
# Test select.select() with empty lists of file descriptors.
select.select([], [], [])
select.select([], [], [], 0.0)
select.select([], [], [], 0.1)
select.select([], [], [], None)
select.select([], [], [], -1.0)
# Test select.select() with a non-empty list of file descriptors.
r, w, x = select.select([0], [1], [2])
r, w, x = select.select([0], [1], [2], 0.0)
r, w, x = select.select([0], [1], [2], 0.1)
r, w, x = select.select([0], [1], [2], None)
r, w, x = select.select([0], [1], [2], -1.0)

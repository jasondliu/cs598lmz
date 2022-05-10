import select
# Test select.select for file descriptor masking.
if not hasattr(select, 'pipemask'):
    raise ImportError("test skipped because select.pipemask not defined")
import os
select.pipemask # ensure it's there

p1, p2 = os.pipe()
fds = [p1, p2]
(r, w, x) = read, write, except
readwrite = range(len(fds) * 2)
print(r, w, x)

select.select(r, w, x)
select.select(r[-1:], w[-1:], x[-1:])
select.select(r[:-1], w[:-1], x[:-1])
select.select(r[:1], w[:1], x[:1])

# make sure all of the file descriptors are accounted for
seen = [0] * max(fds)
for l in [r, w, x]:
    for n in l:
        seen[n] += 1
assert seen == [1] * len(seen)



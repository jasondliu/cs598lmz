import select
# Test select.select() with multiple invalid file descriptors
for r in (()), (3, 4):
    k = select.select(r, r, r)

import select
# Test select.select() with the error return condition.
#
# Get the list of all file descriptors that can be read.
r, _, _ = select.select(range(200), [], [], 0)
if r:
    print('The select() call returned non-empty lists.')
else:
    print('The select() call returned empty lists.')

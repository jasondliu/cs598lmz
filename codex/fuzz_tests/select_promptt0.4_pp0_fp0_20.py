import select
# Test select.select() with an invalid file descriptor.
try:
    select.select([], [], [], 0, -1)
except ValueError:
    pass
else:
    print('ValueError not raised')

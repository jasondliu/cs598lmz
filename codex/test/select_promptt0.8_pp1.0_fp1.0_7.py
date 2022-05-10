import select
# Test select.select function

# 1, 2 are file objects
(readable, writable, errors) = select.select( [1, 2], [], [] )
print(readable)
print(writable)
print(errors)

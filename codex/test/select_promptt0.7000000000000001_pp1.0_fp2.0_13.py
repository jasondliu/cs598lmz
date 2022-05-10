import select
# Test select.select

# Returns 1 if the file descriptor is readable or writable.
# Returns 0 if the timeout expires.
# Returns -1 if the file descriptor is invalid or on error.

# The timeout is specified in seconds (as a float).
# A timeout of 0 waits indefinitely.

# The return value contains three lists of file descriptor.
(r, w, e) = select.select([2], [3], [], 5)


import select
# Test select.select for infinite timeout.
# On some platforms, this will hang forever, but it should not.

# The test should run in under 30 seconds.
timeout = 30
end_time = time.time() + timeout

r, w, e = select.select([], [], [], None)

# This will raise an AssertionError if the test fails.
assert time.time() < end_time

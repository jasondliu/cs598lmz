import select
# Test select.select()

# This test is not complete.  It only tests that select.select()
# doesn't crash.  It doesn't test that it works correctly.

import select

# Make sure we can call select.select() with a timeout of 0.0
select.select([], [], [], 0.0)

# Make sure we can call select.select() with a timeout of None.
select.select([], [], [], None)

# Make sure we can call select.select() with a timeout of > 0.0.
select.select([], [], [], 0.1)

import select
# Test select.select() with a timeout of 0.
#
# This test is not very useful, but it is here to check that the function
# does not crash.

import select

select.select([], [], [], 0)

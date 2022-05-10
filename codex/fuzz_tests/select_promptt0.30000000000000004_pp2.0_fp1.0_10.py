import select
# Test select.select with an empty list of file descriptors.
# This is a regression test for SF bug #813892.
select.select([], [], [], 0)

import select
# Test select.select function

read, write, error = select.select([], [], [], 1)

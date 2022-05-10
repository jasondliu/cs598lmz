import select
# Test select.select with a bad timeout
try:
    select.select([], [], [], 0.5)
except ValueError:
    pass
try:
    select.select([], [], [], -1)
except ValueError:
    pass

# Test the select.poll class
p = select.poll()

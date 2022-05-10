import select
# Test select.select with invalid types
try:
    select.select(1, 2, 3, 4, 5)
except TypeError:
    pass

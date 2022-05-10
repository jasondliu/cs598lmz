import select
# Test select.select([], [], [], 0)
select.select([], [], [], 0)

# Test select.select([], [], [], -1)
select.select([], [], [], -1)

# Test select.select([], [], [], -1.1)
try:
    select.select([], [], [], -1.1)
except ValueError as e:
    print(e)

# Test select.select([], [], [], None)
try:
    select.select([], [], [], None)
except TypeError as e:
    print(e)

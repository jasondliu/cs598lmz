import select
# Test select.select() with an empty timeout
# It should return immediately, not raise an exception
select.select([], [], [], 0.0)

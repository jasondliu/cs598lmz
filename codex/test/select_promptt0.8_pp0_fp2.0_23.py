import select
# Test select.select([], [], [], 5) on an empty array.
select.select([], [], [], 5)
# Test select.poll() on an empty poll set
p = select.poll()
p.poll()
p.poll(5)

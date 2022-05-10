import select
# Test select.select().
print(select.select([], [], [], 0))
print(select.select([], [], [], 0))

# Test the internal self-pipe used by select.select().
r, w = os.pipe()
select.select([r], [], [], 0)

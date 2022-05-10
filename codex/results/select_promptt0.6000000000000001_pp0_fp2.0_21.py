import select
# Test select.select()

# Should return immediately, no block
print(select.select([],[],[],0))

# Should block forever
# print(select.select([],[],[],None))

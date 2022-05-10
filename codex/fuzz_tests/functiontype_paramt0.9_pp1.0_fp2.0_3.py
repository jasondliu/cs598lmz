from types import FunctionType
list(FunctionType(lambda:'',globals(),globals()) for _ in range(2)) == []

# After the tuple normalization we have a constant empty tuple. This
# has been removed. We used to have:
# 5 POP_TOP
# 2 UNPACK_SEQUENCE 0

# Before we used to have this (we have removed constants tuples):
# 1 POP_TOP

# We used to have this test (the LOAD_GLOBALs have been removed here)
# 2 UNPACK_SEQUENCE 0

print('TEST SUCEEDED')

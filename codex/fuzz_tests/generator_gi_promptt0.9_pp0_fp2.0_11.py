gi = (i for i in ())
# Test gi.gi_code.co_name
g1 = (i for i in range(5))
# Test g2.gi_code.co_name
g2 = (i for i in range(5))

# Make sure we have new objects
assert g1.gi_code is not g2.gi_code

# Evaluating the same generator expression creates 2 separate generators (with
# different gi_code objects)
g3 = eval('(i for i in range(5))')
assert g1.gi_code is not g3.gi_code

# Evaluating the same generator expression creates 2 separate generators (with
# different gi_code objects)
g4 = eval('(i for i in range(5))')
print('g4:', g4)
assert g1.gi_code is not g4.gi_code

# Same again
for i in range(4):
    print('i:', i)
    print('========================\n')
    g5 = (i for i in range(5))
    print(g5)
    print('g5.gi_code:', g

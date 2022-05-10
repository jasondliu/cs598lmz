gi = (i for i in ())
# Test gi.gi_code (code object of generator)
print(gi.gi_code)

def print_code(co):
    print("name =", co.co_name)
    print("filename =", co.co_filename)
    print("line # =", co.co_firstlineno)
    print("\nbytecode:\n", co.co_code)

print_code(gi.gi_code)

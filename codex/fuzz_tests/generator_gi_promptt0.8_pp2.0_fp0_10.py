gi = (i for i in ())
# Test gi.gi_code.co_name
print(gi.gi_code.co_name)
# Test gi.gi_code.co_argcount
print(gi.gi_code.co_argcount)
# Test gi.gi_code.co_varnames
print(gi.gi_code.co_varnames)

print("-" * 20)

# Test sys.path
print(sys.path)

print("-" * 20)

# Test sys.flags
print("Interactive" in sys.flags)
print("Debug" in sys.flags)

print("-" * 20)

# Test sys.modules
print("sys" in sys.modules)
print("os" in sys.modules)

print("-" * 20)

# Test sys.exc_info
try:
    1 / 0
except ZeroDivisionError:
    print("ZeroDivisionError")
    print("Type: {} - Reason: {}".format(sys.exc_info()[0], sys.exc_info()[1]))

print("-" * 20)

# Test sys

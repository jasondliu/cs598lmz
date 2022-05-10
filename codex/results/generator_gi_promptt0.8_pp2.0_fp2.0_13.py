gi = (i for i in ())
# Test gi.gi_code
print(gi)
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>

# Test gi.gi_frame
print(gi.gi_frame)  # Output: <frame object at 0x0000000002EBF048>

# Test gi.gi_running
print(gi.gi_running)  # Output: False

# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)  # Output: None

print()

# create a generator with next()
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# It returns an object but does not start execution immediately.
a = my_gen()

# We can iterate through the items using next().
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and

gi = (i for i in ())
# Test gi.gi_code attribute
print(f"gi.gi_code = {gi.gi_code}")

# print generator
gen = (x for x in (1, 2, 3))
print(gen)

# num_gen is a generator object
num_gen = (num for num in range(5))
print(num_gen)

# accessing the values of generator
for num in num_gen:
    print(num)

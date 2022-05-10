gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("SKIP")
    raise SystemExit

print("not_iterable", end=" ")
for x in [123, "abc"]:
    try:
        list(x)
    except TypeError:
        print("pass")
    else:
        print("TypeError not raised")

print("iter_len", end=" ")
for x in [[1, 2], "ab", (1, 2, 3), {}]:
    try:
        print(len(iter(x)))
    except TypeError:
        print("TypeError")

print("iter_len_func", end=" ")
for x in [[1, 2], "ab", (1, 2, 3), {}]:
    try:
        print(len(iter(lambda: x, 0)))
    except TypeError:
        print("TypeError")

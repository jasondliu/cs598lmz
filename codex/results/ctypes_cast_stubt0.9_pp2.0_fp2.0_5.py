import ctypes
ctypes.cast(m, ctypes.py_object).value

# %%
snip = m[:100].reshape((10, 10))

# %%
fmt = """\
{x:<8}""" + """"{y:<9}""" + " ".join("{v:>7.3f}" for _ in range(8)) + "\n"

print("\n=====\n")
for r in snip:
    for i, v in enumerate(r):
        print(fmt.format(x=i, y=int(v), v=v))
print("\n=====\n")

# %%
with open("b.txt", "w") as f:
    f.write(utils.serialize(m))

# %%
m2 = utils.deserialize(open("b.txt").read())

# %%
m

# %%
m2

# %%

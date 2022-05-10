import types
types.SimpleNamespace()

# %%
class Struct(object):
    pass

raw = Struct()
raw.to_csv = (lambda x: "".join(x.split("/")[-1:])).__get__(raw)
raw.to_csv("./tmp")

# %%

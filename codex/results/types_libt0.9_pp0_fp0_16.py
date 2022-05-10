import types
types.MethodType(lambda: [], str)
types.MethodType(lambda: [], list)

# %%
types.MethodType(lambda: [], tuple)


# %%
class MyList(list):
    def __iter__(self):
        return iter([3,4,5])

list(MyList())


# %%

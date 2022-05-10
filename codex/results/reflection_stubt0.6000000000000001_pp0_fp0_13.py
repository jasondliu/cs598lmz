fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
# fn()

# from collections import UserDict

# class MyDict(UserDict):
#     def __getitem__(self, key):
#         return super().__getitem__(key)
#     def __missing__(self, key):
#         return key

# d = MyDict({"a": 1, "b": 2})
# print(d["a"])
# print(d["c"])

# from collections import defaultdict
# d = defaultdict(list)
# d["a"].append(1)
# d["a"].append(2)
# d["b"].append(4)
# print(d)

# from collections import OrderedDict
# d = OrderedDict()
# d["foo"] = 1
# d["bar"] = 2
# d["spam"] = 3
# d["grok"] = 4
# # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
# for key in d:
#     print(key, d[

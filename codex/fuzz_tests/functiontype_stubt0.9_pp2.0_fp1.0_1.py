from types import FunctionType
a = (x for x in [1])
b = (x for x in range(4))
c = (x for x in range(4))
d = (x for x in range(2))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))
print(isinstance(d, FunctionType))

print(a.gi_frame.f_code)
print(b.gi_frame.f_code)
print(c.gi_frame.f_code)
print(d.gi_frame.f_code)


# class Solution:
#     def __init__(self):
#         self.dic = {}
#
#     def kWeakestRows(self, mat: list, k: int) -> list:
#         if len(mat) < k:
#             return []
#         if len(mat) == k:
#             return list(range(len(mat)))
#
#         for i, items in enumerate(mat):
#             if i in self.dic.keys():
#                 continue

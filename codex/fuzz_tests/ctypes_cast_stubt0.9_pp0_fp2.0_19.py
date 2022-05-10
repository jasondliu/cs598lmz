import ctypes
ctypes.cast(None, ctypes.py_object)
s = {1: "abcabcad"}
print(s)
s1 = {2: "abc"}
s.update(s1)
print(s)
s = ["Hello", " how", " are", " you"]
s1 = ["Hello", " how", " are", " you"]
print(id(s))
print(id(s1))
s = (1, 2, 3, 4)
s1 = (1, 2, 3, 4)
print(id(s))
print(id(s1))
a = int(input())
b = int(input())
if a == b:
    print('0')
else:
    if a > b:
        print(a)
    else:
        print(b)

a = int(input())
b = int(input())
if a == b:
  print("0")
else:
  if a > b:
    print(a)
  else:
    print(b)

a = int(input())
b = int(input())


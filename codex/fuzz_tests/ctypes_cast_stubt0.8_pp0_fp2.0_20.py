import ctypes
ctypes.cast(id(a), ctypes.py_object).value

#%%

a = 20
a = "The quick brown fox."
print(a)

#%%

a = "The quick brown fox."
b = a.encode()
print(a)
print(b)
print(b.decode())

#%%
# Python Strings

print("Hello, World!")

#%%

print("Hello, World!")
print('Hello, World!')

#%%

print("Hello, World!")
print('Say hi to Bob\'s mother.')
print("Say hi to Bob's mother.")
print('So, he said "hi".')
print("So, he said \"hi\".")
print('So, he said "hi".')
print("So, he said \"hi\".")

#%%

print("Hello, World!")
print('Hello, World!')

#%%

a = "Hello, World!"
print(a[1])

#%%

a = "Hello, World!"
print(a[2:5

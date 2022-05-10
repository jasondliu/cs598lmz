from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_freevars)

#%%
for i in range(10):
    print(i)

#%%
a = 'hi'
b = 'hi'
print(a==b)
print(a is b)

#%%
a = True
b = True
print(a==b)
print(a is b)

#%%
a = 1
b = 1
print(a==b)
print(a is b)

#%%
a = 0
b = 0
print(a==b)
print(a is b)

#%%
a = 1.
b = 1.
print(a==b)
print(a is b)

#%%
a = 1.
b = 1.
print(a==b)
print(a is b)

#%%
a = 1.
b = float(1)
print(a==b)
print(a is b)

#%%
a = 1.
b = 1.
print(a==b)
print(a is b

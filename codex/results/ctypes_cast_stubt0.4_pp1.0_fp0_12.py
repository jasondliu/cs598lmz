import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
x = [1,2,3]
i = 0
def f():
    print(x[i])
    i += 1
f()

#%%
def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)

plus_3(4)
plus_5(4)

#%%
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#%%
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#%%
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):


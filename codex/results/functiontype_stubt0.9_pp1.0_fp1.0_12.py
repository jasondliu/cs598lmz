from types import FunctionType
a = (x for x in [1])

a.close()
a.throw()
a.__next__()

# %% [markdown]
# if, else, elif

# %%
if True:
    print('true')

# %%
if False:
    print('false')

# %%
if True:
    print('true')
else:
    print('false')

# %%
if False:
    print('true')
else:
    print('false')

# %%
if False:
    print('true')
elif True:
    print('elif')
else:
    print('false')

# %%
i = 1
if i == 0:
    print('0')
elif i == 1:
    print('1')
else:
    print('none of the above')

# %% [markdown]
# for/else

# %%
for i in [1, 2, 3]:
    print(i)
else:
    print('end')

# %%
for i in range(5):
    if i == 5:
        print('end

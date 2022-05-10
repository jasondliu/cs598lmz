from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

#%% [markdown]
# ### Defining a function with a single positional parameter

#%%
def quotient(x, y):
    return x / y


quotient(2, 3)

#%% [markdown]
# ### Defining a function with a single keyword parameter

#%%
def power(base, exponent=2):
    return base ** exponent


power(3)

#%%
power(3, 3)

#%% [markdown]
# ### Defining a function with a single default parameter

#%%
def quotient(x=1, y=1):
    """Return the quotient of its two arguments."""
    return x / y


quotient()  # 1
quotient(2)  # 2.0
quotient(2, 3)  # 0.6666666666666666
power(3, 3)  # 27

#%% [markdown]
# ### Defining a function with two parameters

#%%
def power(base, exponent):


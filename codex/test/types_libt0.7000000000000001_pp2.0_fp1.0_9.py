import types
types.MethodType(None, None)

# %%
def hello(name):
    print('Hello, %s' % name)
    
    
# %%
hello('World')


# %%
(lambda x: x + 1)(2)


# %%
def get_hello():
    return lambda x: x + 1


# %%
get_hello()(2)


# %%
def get_add(n):
    return lambda x: x + n


# %%
add_1 = get_add(1)
add_1(2)


# %%
add_2 = get_add(2)
add_2(2)


# %%
def get_add_list():
    add_list = []
    for i in range(1, 4):
        add_list.append(get_add(i))
    return add_list


# %%
add_list = get_add_list()
for add in add_list:
    print(add(2))


# %%
add_list[0](2)


# %%

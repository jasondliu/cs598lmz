import ctypes
ctypes.addressof(first)

# %%
second = int(input("Please enter a value: "))

# %%
def first_function():
    print("This is my first function!")

# %%
for i in range(5):
    first_function()

# %%
def say_hello_to(name):
    print("Hello", name)

# %%
say_hello_to("Brian")

# %%
say_hello_to("Susan")

# %%
say_hello_to("Mark")

# %%
say_hello_to(name="Mark")

# %%
say_hello_to(name="John", surname="Smith")

# %%
def add_two_numbers(first, second):
    return first + second

# %%
add_two_numbers(1, 2)

# %%
def add_two_numbers(first, second):
    return first + second

# %%
add_two_numbers(2, 3)

# %%
def say_hello_to(name, surname):
    print

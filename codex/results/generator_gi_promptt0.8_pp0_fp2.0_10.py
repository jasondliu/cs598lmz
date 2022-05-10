gi = (i for i in ())
# Test gi.gi_code:
gi.gi_code


def func():
    print("hello")


print(func)

# Test code_obj.co_zombieframe
print(func.__code__.co_zombieframe)


def func():
    pass


# Test code_obj.co_stacksize
print(func.__code__.co_stacksize)


def func():
    pass


# Test .gi_frame and .f_code
def func():
    print(func.__code__)


func()

# Test .gi_frame and .f_code
def func():
    print(func.__code__.co_zombieframe)


func()

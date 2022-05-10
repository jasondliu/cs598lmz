import threading
threading.Thread(target=print_cube, args=(10,)).start()


# 1.6   function call using keyword arguments
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


print_kwargs(a=1, b=2, c=3)

# 1.7   function call using a mix of positional and keyword arguments
def print_values(a=1, b=2, c=3):
    print('a=', a, 'b=', b, 'c=', c)


print_values(a=10, c=50)

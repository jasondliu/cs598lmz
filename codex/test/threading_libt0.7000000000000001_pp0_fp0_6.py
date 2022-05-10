import threading
threading.stack_size(67108864)


def func(x):
    return x * 2


if __name__ == "__main__":
    # Define an input sequence.
    l = [1, 2, 3, 4, 5]

    # star map() is used when argument function to be mapped takes more than 1 arguments.
    # The way star map works is it breaks down the iterable given to it,
    # and passes it as positional arguments.
    result = map(func, l)

    print(list(result))

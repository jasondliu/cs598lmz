fn = lambda: None
# Test fn.__code__.co_argcount
# num_args = fn.__code__.co_argcount
# num_args = 10
# fn.__code__.co_argcount = num_args
# fn.__defaults__ = [None for _ in range(num_args)]

print("Write a program to sort three integers without using conditional statements and loops.\n")
def sort_integers(a, b, c):
    """Sort three integers without using conditional statements and loops."""
    # return sorted([a, b, c])
    items = [a, b, c]
    greater = max(items)
    lesser = min(items)
    mid = items[3 - greater - lesser]
    return [greater, mid, lesser]
print(sort_integers(0, -1, 1))

# def calculate_integers(a, b, c):
#     """Calculate value of three integers."""
#     # return max(a, b, c) - min(a, b, c)
#     items = [a, b, c]
#     greater

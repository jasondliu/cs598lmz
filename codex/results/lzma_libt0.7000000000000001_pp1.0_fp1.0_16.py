import lzma
lzma_dir = lzma.LZMADecompressor()

# to make an iterator: use iter(thing)
# to get an iterator's next item: use next(thing)
# to get all items: use list(thing)

# to test whether an object is an iterator use collections.Iterator
# e.g. isinstance(obj, collections.Iterator)

# to get the next item from an iterator, use next(iterator)

# list comprehensions can be used to get a list from an iterator
# list comprehensions can consist of a single line, or an expression followed by for,
# followed by zero or more for or if clauses. The result will be a new list resulting
# from evaluating the expression in the context of the for and if clauses which follow it.
# The list comprehension always returns a result list.

# generator expressions return an iterator that computes the values as necessary, not needing
# to materialize all the values at once.

# Generator expressions are surrounded by parentheses (...),
# where a list comprehension is surrounded by brackets [...].

# both generator expressions and list comprehensions can be used

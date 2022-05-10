import threading
threading.Thread()

import multiprocessing
multiprocessing.Process()

############################ 42 ############################
# Assuming a is a list of lists, that contains integer lists of even length,
# a = [[1, 2, 4], [4, 2, 1], [5, 6, 7, 8]]
# flatten a into a single dimensional list using list comprehensions.
a = [[1, 2, 4], [4, 2, 1], [5, 6, 7, 8]]
a_flat_list=[x for sublist in a for x in sublist]

# Using recursion and an accumulator
def flatten(a):
    def flatten_sub_list(sublist,accum):
        for x in sublist:
            if type(x)==list:
                flatten_sub_list(x,accum)
            else:
                accum.append(x)
        return accum

    return flatten_sub_list(a,[])


############################ 43 ############################
# Given a function f, and N return a debounced f of N milliseconds

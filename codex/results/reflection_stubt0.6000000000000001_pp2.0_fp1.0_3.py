fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()"""

#python -m timeit -n 10000 -r 100 -s """
#from collections import namedtuple
#from random import randint
#
#def get_namedtuple():
#    return namedtuple('named', 'a b c d e')(randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000))
#
#def get_tuple():
#    return (randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000))
#
#def get_list():
#    return [randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000)]
#
#def get_dict():
#    return {'a': randint(0,1000), 'b': randint(0,1000), 'c': randint(0,1000), 'd': randint(0,1000),

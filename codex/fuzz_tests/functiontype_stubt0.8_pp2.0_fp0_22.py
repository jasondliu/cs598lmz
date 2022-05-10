from types import FunctionType
a = (x for x in [1])
b = (x for x in [1,2,3])
c = (x for x in [1,2,3,4,5,6,7,8])
d = (x for x in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

def Q(iterable):
    '''
    Q(iterable) -> True or False

    '''
    while True:
        try: first = next(iterable)
        except StopIteration: break
        else:
            if first == None: return False
    else: return True

def empty(iterable):
    '''
    empty(iterable) -> True or False

    '''
    try: first = next(iterable)
    except StopIteration: return True
    else: return False

def _next(iterable):
    '''
    _next(iterable) -> next of iterable
    '''
    return next(iterable)

def nth(iterable, n):
    '''

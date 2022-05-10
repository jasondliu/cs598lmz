fn = lambda: None
# Test fn.__code__
#     print('Test fn.code')
#     print('\tf.__code__: ', fn.__code__)
#     print('\tsizeof(f.__code__):', sys.getsizeof(fn.__code__))
#     print('\tnbytes: ', sys.getsizeof(fn.__code__.co_code))
# Test fn.__globals__
#     print('Test fn.__globals__')
#     print('\tfn.__globals__:', fn.__globals__)
#     print('\tsizeof(fn.__globals__): ', sys.getsizeof(fn.__globals__))


def measure_object_size(obj, deep=False, is_print=True,
                        indent='', tab='    '):
    if deep:
        func = sys.getsizeof
    else:
        func = lambda x: 0
    if is_print:
        print(indent + type(obj).__name__ + ': ' + str(func(obj)))


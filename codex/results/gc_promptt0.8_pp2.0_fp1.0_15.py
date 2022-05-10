import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().  We test leaks by counting the number of allocated
# types before and after a gc.collect().


def test_func():
    n = sys.gettotalrefcount()
    gc.collect()
    m = sys.gettotalrefcount() - n
    if verbose:
        print('collected %d references' % m)
    gc.collect()
    return m


type_list = []
list_list = []
dict_list = []
for o in range(10):
    type_list.append(type('type%d' % o, (object,), {}))
    list_list.append([])
    dict_list.append({})
test_func()
list_list[7].append(list_list)
dict_list[8]['dict'] = dict_list
type_list[9].__dict__.update({'type': type_list})
test_func()
del list_list
del dict_list
del type_list
test_func()
del n, m, o
test_func()
print('done')
#

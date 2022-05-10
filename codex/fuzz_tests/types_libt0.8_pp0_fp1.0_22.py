import types
types._SymbolClass = types.SymbolType
del types

#def all_equal(iterable):
#    i, iterable = itertools.tee(iterable)
#    try:
#        first = next(i)
#    except StopIteration:
#        return True
#    return all(first==rest for rest in i)
#
#def check_list_format(l):
#    if not isinstance(l, list):
#        raise ValueError("Expected list, got %s." % (l,))
#    if not all_equal(len(e) for e in l):
#        raise ValueError("Expected list of uniform length.")
#
#def chain_lists(lists):
#    return list(itertools.chain(*lists))
#
#def split_lists(lists, lengths):
#    if len(lists) != len(lengths):
#        raise ValueError("Expected lengths to be of equal length.")
#    i = iter(lists)
#    for n in lengths:
#        yield [next(i) for _

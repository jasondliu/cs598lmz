fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

print(fn())
print(fn.__code__)

#test_sorted_set_operations_on_bytes

print(sorted(set(b'abc') | set(b'def')))
print(sorted(set(b'abc') & set(b'def')))
print(sorted(set(b'abc') - set(b'def')))
print(sorted(set(b'abc') ^ set(b'def')))

print(sorted(set(b'abc') | set([1, 2, 3])))
print(sorted(set(b'abc') & set([1, 2, 3])))
print(sorted(set(b'abc') - set([1, 2, 3])))
print(sorted(set(b'abc') ^ set([1, 2, 3])))

print(sorted(set([1, 2, 3]) | set(b'def')))
print(sorted(set([1, 2, 3]) & set(b'def')))
print(

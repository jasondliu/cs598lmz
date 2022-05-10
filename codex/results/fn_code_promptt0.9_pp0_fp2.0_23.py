fn = lambda: None
# Test fn.__code__.co_name
string_tests.append((fn.__code__.co_name, 'None'))
# Test fn.__code__.co_argcount
string_tests.append((fn.__code__.co_argcount, '0'))

# Test co_consts
tuple_of_strings = (1, 2.0, '3', '4')
fn3 = test_co_consts.fn3
string_tests.append((fn3.__code__.co_consts[3], tuple_of_strings))
string_tests.append((repr(fn3.__code__.co_consts[3]), str(tuple_of_strings)))

def test(n):
    fn.__code__.co_argcount + n
    fn.__code__.co_name + n
    f(*(fn.__code__.co_consts[3]), **{'separator':'|'}) + n
    return n
fn.__code__.co_argcount + 1
fn.__code__.co_name + 1

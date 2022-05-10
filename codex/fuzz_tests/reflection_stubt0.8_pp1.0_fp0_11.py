fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    dis.dis(fn)
except TypeError as e:
    print(e.__class__.__name__ + ':', e)

print('')

# test_code_to_index
print('TEST: test_code_to_index')
def fn():
    pass
print(dis.code_to_index(fn.__code__))

print('')

# test_dis
print('TEST: test_dis')
def fn():
    a = 1
    b = 2
    c = 3
print(dis.dis(fn))

print('')

# test_show_code
print('TEST: test_show_code')
dis.show_code(fn)

print('')

# test_get_instructions
print('TEST: test_get_instructions')
def fn():
    return 1

# get_instructions(fn)
print(dis.get_instructions(fn))

print('')

# test_instruction_from

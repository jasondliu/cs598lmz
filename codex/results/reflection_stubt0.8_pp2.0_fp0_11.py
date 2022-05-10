fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
'''

# -- 02_pep_control_flow --

# -- 02_01_while --

print('\n')
print('-' * 40)
print(f'{"02_01_while":^40}')
print('-' * 40)

while True:
    pass

b = True

while b:
    pass

b = b.__xor__(b)

print('\n')

# -- 03_01_for --

print('-' * 40)
print(f'{"03_01_for":^40}')
print('-' * 40)

for x in range(3):
    print(x)

print('\n')

for x in 'abc':
    print(x)

print('\n')

for x in range(3):
    print(x)
    break

print('\n')

print('\n')

for x in range(3):
    print(x)
else:
    print('finally')

print('\

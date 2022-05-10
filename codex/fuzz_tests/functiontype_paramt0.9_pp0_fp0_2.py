from types import FunctionType
list(FunctionType('bogus'))  # Do not crash

for ch in 'abcdefghijklmnopqrstuvwxyz':
    for n in range(1,50):
        s = ch * n
        list(s)  # Check string-like things over our code coverage edge

print('Tests completed')

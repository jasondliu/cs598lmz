from _struct import Struct
s = Struct.__new__(Struct)
s.add('I', 'primes')
s.add('O', 'range')
s.build(b)
display(s)

i = 80
x = s.offset('I')
print(hex(x))
print(hex(i<<5))
r = i<<5 + x

print(hex(r))
print(r)
w = 64
r = r + (r+r&r)&((r&r)<<w-r)&((r&r)>>w-r+1)
print(hex(r))
print(r)
def div1(int_val, div_val=3):
    return int_val / div_val
def div2(int_val, int_val2=1, div_val=3):
    return int_val / int_val2 / div_val
%timeit div1(1000000007)
%timeit div2(1000000007)
s = 657
i = 117
origin = 65
ord_ = ord
chr_ = chr
instr = {}
for x in range

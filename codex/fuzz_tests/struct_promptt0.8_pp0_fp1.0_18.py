import _struct
# Test _struct.Struct() arg
print(_struct.Struct('i').size)
# 2
print(_struct.Struct('L').size)
# 4
print(_struct.Struct('q').size)
# 8
print(_struct.Struct('Q').size)
# 8
</code>
Running this on my machine I get 4, 8, 8 and 8.
What processor are you running on?  Its possible it has 128 bit <code>long</code>s.


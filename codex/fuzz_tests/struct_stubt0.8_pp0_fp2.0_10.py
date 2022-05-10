from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I'
for i in xrange(64):
    try:
        s.size = i
    except ValueError as e:
        print(e)
        break
    else:
        s.size = s.size + 1
</code>
Output:
<code>size too big
</code>


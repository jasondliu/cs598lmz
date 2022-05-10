from _struct import Struct
s = Struct.__new__(Struct)
s
s.format = '12s 12s if'
s.size = s.calcsize(s.format)

f = open('myfile.txt', 'r')

for line in f.readlines():
    data = line.strip().split()
    print(data)

    # I'm adding code ref: Python Cookbook 2nd Ed page 507
    f1 = data[0]
    f2 = data[1]
    f3 = int(data[2])
    f4 = float(data[3])
    # convert to bytes
    bytes = s.pack(f1,f2,f3,f4)
    # I'm adding code ref: Python Cookbook 2nd Ed page 507
    print("bytes: {}".format(bytes))
</code>
I get error message with this code:
<code>bytes: b'abcdefghabcdefgh\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x85\xe0\x00\x00\x00\x

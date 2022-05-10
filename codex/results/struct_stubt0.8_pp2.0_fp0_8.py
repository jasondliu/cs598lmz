from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')

for _ in range(int(input())):
    print(s.pack(*map(int, input().split())))

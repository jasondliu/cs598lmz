from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('BB')

region1 = '''Header
H  16h
B  2
B  1
H  2
H  2
H  150
H  150
B  1
B  1
B  1
B  1
H  6
i  3
B  1
B  1
H  1
B  1
H  2
H  1
B  1
i  100
B  1
B  1
H  1
B  1
H  2
H  1
B  1
B  1
H  1
B  1
i  3
f  50
B  1
B  1
H  1
B  1
B  1
B  1
H  1
B  1
H  1
b  1
B  1
H  1
i  240
f  3
B  1
b  1
B  1
H  1
H  1
B  1
H  1
b  1
B  1
H  1
i  240
f  3


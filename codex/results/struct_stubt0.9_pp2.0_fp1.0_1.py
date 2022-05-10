from _struct import Struct
s = Struct.__new__(Struct)
s.format = "I5sx"
s.size = s.calcsize(s.format)

f = open(filename, 'rb')
for i in xrange(orders_count):
    if i % 1000000 == 0:
        print(i)
    f.seek(s.size * i)
    b = f.read(s.size)
    (time, key) = s.unpack(b)
    if time in times:
        times[time].append(key)
    else:
        times[time] = [key]

count = 0
for i in xrange(orders_count):
    if count > 100:
        break
    if i % 1000000 == 0:
        print(i)
    f.seek(s.size * i)
    b = f.read(s.size)
    (time, key) = s.unpack(b)
    if time in times and key in times[time]:
        count += 1
        print(count, i, time, map(ord, key))
        
count = 0

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')

t1 = time.time()

with open(sys.argv[2], 'wb') as f:
    for v in data:
        f.write(s.pack(v))

t2 = time.time()

print('{}生成文件耗时{}'.format(sys.argv[2], t2 - t1))

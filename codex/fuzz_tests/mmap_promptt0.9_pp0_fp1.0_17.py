import mmap
# Test mmap.mmap() performance
mm = mmap.mmap(-1, 10*4)
for extra_precision in [0, 1, 2]:
    for precision in [32, 64]:
        for ieee in [0, 1]:
            bytes = mm[:precision >> 3]
            for i in range(int(10/len(bytes))):
                mm.seek(0, 0)
                mm.write(struct.pack('B'*len(bytes), *bytes))
            mm.seek(0, 0)
            d = struct.unpack('B'*len(bytes), mm.read(len(bytes)))
            val = struct.pack('B'*len(d), *d)
            result = struct.unpack(f'{1 if ieee else "="}f', val if precision == 32 else val + val[:4])[0]
            optimal_precision_for_value(result, extra_precision)
            mm.seek(0, 2)
            mm.write(struct.pack(f"BBBBBBBBH", *[255, 255, 255, 255

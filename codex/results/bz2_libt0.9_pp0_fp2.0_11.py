import bz2
bz2.BZ2File(fnstarbz, mode='r', compresslevel=9)

bc.strategy = 'BZ_FILE_I'
bc.write_output_file(Star, './starbz')
fnstarbz = './starbz'
%time bparbz = read_binary_file_doubles(fnstarbz, Ntot_star*2)
%time for i in range(100): read_binary_file_struct(fnstarbz, Ntot_star*2)

import msgpack
import bz2
try:
    d = msgpack.packb(bc.OStruct, use_bin_type=True)
except:
    d = msgpack.packb(bc.OStruct, default=lambda o: o.__dict__, use_bin_type=True)
bz2_bytes = bz2.compress(d)

np.savez_compressed('./starbz2', bz2_bytes=bz2_bytes)

fnstarbz2 = './star

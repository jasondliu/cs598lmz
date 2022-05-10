import mmap
import struct
import sys

def read_data(file_name, n_data, n_channels):
    data = np.empty(n_data * n_channels, dtype=np.float32)
    with open(file_name, 'rb') as f:
        m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        for i in range(n_data):
            for j in range(n_channels):
                # read 4 bytes as float32
                data[i*n_channels + j] = struct.unpack('f', m.read(4))[0]
    return data.reshape((n_data, n_channels))

def write_data(file_name, data):
    with open(file_name, 'wb') as f:
        for i in range(len(data)):
            # write float32
            f.write(struct.pack('f', data[i]))

def read_params(file_name, n_params):
    params = np

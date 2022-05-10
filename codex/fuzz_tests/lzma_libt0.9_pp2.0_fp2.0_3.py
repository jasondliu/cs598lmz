import lzma
lzma_mode = lzma.FORMAT_ALONE | lzma.CHECK_CRC64

import msgpack
import msgpack_numpy as m
m.patch()

import numpy as np
import h5py
import sklearn.preprocessing

from CMB_module.wigner import wigner_transform
from CMB_module.test_variables import variables_smica
from CMB_module.generate_data import check_template

def lzma_compress(filename):
    """ Compress a file with LZMA compression. """
    print("Started compressing {}.".format(filename))
    input_name = "{}.npy".format(filename)
    output_name = "{}.xz".format(filename)
    with open(input_name, 'rb') as input_file:
        with lzma.open(output_name, 'wb', preset=3) as output_file:
            shutil.copyfileobj(input_file, output_file)
    os.remove(input_name)
    print("Compression

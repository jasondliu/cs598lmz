import _struct
import base64
import pdb
import random
import timeit
import time
import binascii

#      __ __
#  \-|__/  \
#   |===\__/

def map(input_file, action, output_file):

    with open(input_file, 'rb') as in_f, open(output_file, 'wb') as out_f:

        for pack in iter(lambda: in_f.read(4), ''):

            if len(pack) < 4:
                break

            pack_iso, = _struct.unpack('<f', pack)

            out_f.write(_struct.pack('<f', run_on_sample(pack_iso, action)))


def run_on_sample(sample, action):

    # pdb.set_trace()
    if action.strip() == 'rs':
        return random.random()

    elif action.strip() == 'is':
        return sample

    else:
        return 0

#       _.-"
#    _.-"  \
#   /      

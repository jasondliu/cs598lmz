import mmap

def generate_pass(pass_len, key_len, passfile):
    print("Generating password...")
    with open(passfile, 'rb') as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        try:
            start = 0
            end = pass_len * key_len
            print("\tstart: {} end: {}".format(start, end))
            assert mm.size() >= end
            pass_bytes = bytearray(mm[start:end])
            print("\tbytes: {}".format(pass_bytes))
            return pass_bytes
        finally:
            mm.close()

def generate_key(key_len, keyfile):
    print("Generating key...")
    with open(keyfile, 'rb') as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

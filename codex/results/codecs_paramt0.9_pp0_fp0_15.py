import codecs
codecs.register_error('euc-jp-ignore', codecs.lookup_error('ignore'))


def find_extensions(directory, extensions):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            base, ext = os.path.splitext(filename)
            if ext.lower() in extensions:
                yield os.path.join(dirpath, filename)


def read_mo_time(f):
    f.seek(0x0c)

    t = unpack('I', f.read(4))[0]
    t += unpack('I', f.read(4))[0]

    return t


def extract_mo(f, en_out, ja_out):
    if f.read(4) != b'\x95\x04\x12\xde':
        raise RuntimeError('MO file is corrupt.')
    f.read(12)

    msg_index_offset, msg_index_length = unpack('II', f.read(8))
    msg_offset, msg_

import _struct
import time


def _unpack(fmt, buf):
    assert len(buf) == struct.calcsize(fmt)
    return struct.unpack(fmt, buf)


def dump(in_path, out_path):
    Logger.info('Parsing input file: {}'.format(in_path))
    with open(in_path, 'rb') as f:
        in_buf = f.read()

    Logger.info('Parsing input file (DONE)')

    with open(out_path, 'w+') as f:
        parse(in_buf, f)

    Logger.info('Dumping done: {}'.format(out_path))


def parse(in_buf, fout):
    pos = 0
    header = in_buf[pos:pos+32]
    pos += 32
    [magic, version, date, modify_date, max_id, count_items, unknown, padding] = _unpack(
        "< 4s L 2x L L 2x H 4x",
        header)

   

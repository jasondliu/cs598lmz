import mmap


def get_max_seq_no(filename):
    max_seq_no = 0
    for packet in log_parser.read(filename):
        seq_no = packet.seq
        if seq_no > max_seq_no:
            max_seq_no = seq_no
    return max_seq_no


def init(filename):
    mm = mmap.mmap(
        -1,
        PAYLOAD_PER_SEQNO * (get_max_seq_no(filename) + 1),
        flags=mmap.MAP_PRIVATE | mmap.MAP_ANONYMOUS,
        prot=mmap.PROT_READ | mmap.PROT_WRITE)
    return mm


def write(mm, seq_no, data):
    off = PAYLOAD_PER_SEQNO * seq_no
    mm[off:off + len(data)] = data


def read(mm, seq_no):
    off = PAYLOAD_PER_SEQNO * seq_no

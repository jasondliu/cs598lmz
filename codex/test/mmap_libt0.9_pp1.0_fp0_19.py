import mmap


def init(filename) :
    mappings = defaultdict(lambda: defaultdict(lambda: defaultdict()))
    for line in open(filename) :
        char, key, entry, value = line.strip().split('\t')
        mappings[char][key][entry] = value
    return mappings


def empty_state() :
    return {'lang': '', 'text': '', 'scheme': '', 'rules': [], 'changes': []}


def decode_input(filename, mappings) :
    state = empty_state()
    fin = open(filename, 'r+b')
    m = mmap.mmap(fin.fileno(), 0)
    m.seek(0)

    for byte in m :
        byte = ord(byte)
        for key, val in mappings[state['scheme']]['5-bits'].iteritems() :
            if byte & int(key) == int(key) :
                state['text'] += val


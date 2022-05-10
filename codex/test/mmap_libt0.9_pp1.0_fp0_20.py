import mmap
import numpy
def parse_lattice(path):
    with open(path) as f:
        s = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        if not (s.readline() == b'%%MatrixMarket matrix coordinate real general\n' and s.readline().startswith(b'%') and s.readline().startswith(b'%')):
            raise ValueError('Unsupported matrix market format')
        chain_size, num_symbols, num_transitions = map(int, s.readline().split())
        lattice = init_lattice(chain_size, num_symbols)
        if not lattice.shape == (chain_size + 1, chain_size + 1):
            raise ValueError('Bad input matrix shape: ' + str(lattice.shape))
        for i in range(num_transitions*3):
            i1, i2, v = map(float, s.readline().split())

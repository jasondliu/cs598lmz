from bz2 import BZ2Decompressor
BZ2Decompressor()

def dcd(path):
    pass

def pdb(path):
    pass

file_suffix = {
    '.dcd': dcd,
    '.pdb': pdb
}


def load_pdb(path):
    atom_lines = []
    xyz = []
    with open(path) as f:
        for line in f:
            if line.startswith('ATOM'):
                atom_lines.append(line)
                if line[21] == '7' or line[21] == '8':
                    continue
                xyz.append([float(line[31:38]), float(line[39:46]), float(line[47:54])])
    return np.array(xyz)

test = load_pdb('neut.1/neut.1.VW.00/neut.1.VW.00.pdb')
test

centers = np.array([[-387.62356, -457.6278, -630.45435], [-436.96033, -594.9165, -

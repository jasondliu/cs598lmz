import io
class File(io.RawIOBase):
    def __init__(self,fname):
        self.f = open(fname,'r')
    def read(self,n):
        return self.f.read(n)
    def seek(self,n):
        self.f.seek(n)
    def tell(self):
        return self.f.tell()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python fix_offset.py path_to_noperm_file path_to_perm_file")
        exit()

    print('Converting lammps bop file:',sys.argv[1])
    no_perm = File(sys.argv[1])
    perm = File(sys.argv[2])
    perm_size,_ = read_forces_size(perm)
    perm_size *= -perm.tell()

    no_perm.seek(0,2)
    no_perm_size = no_perm.tell()
    no_perm.seek(0)

    perm.seek

import mmap

### global variables
data_dir = "/home/gary/data/"

def get_data_folder():
    global data_dir
    return data_dir

def get_fname(pdbid, rec, lig, fix=False, zipped=False):
    """Find PDB structure file name given pdbid, receptor, and ligand
    """
    out_str = pdbid + "-" + rec + "-" + lig
    if fix:
        out_str += "-fix"
    if zipped:
        out_str += ".gz"
    else:
        out_str += ".pdb"
    return out_str

def get_fname_offset(fname):
    """Get offset of the structure file from the header file
    """
    fname = data_dir + fname + ".txt"
    with open(fname, "r") as f:
        offset = int(f.read())
    return offset

def get_header(fname):
    """Get header from structure file
    """
    header = ""
    fname

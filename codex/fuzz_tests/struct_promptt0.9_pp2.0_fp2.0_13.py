import _struct
# Test _struct.Struct >>
def test1():
    f = open("../sto_files/interface.sto")
    lines = f.readlines()
    f.close()
    structure = Sto_parser.base(lines)
    for atom in structure.natoms:
        print atom


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print "Test _struct"
f = open("../sto_files/interface.sto")
lines = f.readlines()
f.close()
structure = Sto_parser.base(lines)

struc = _struct.Structure()
struc.create_from_sto(structure)
struc.printer()
struc.terminal_print()
struc.parser()
struc.set_cell(10,10,10)
struc.printer()
struc.set_centroid(0,0,0)
struc.printer()
struc.set

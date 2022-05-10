import _struct
# Test _struct.Struct >>
def test1():
    f = open("../sto_files/interface.sto")
    lines = f.readlines()
    f.close()
    structure = Sto_parser.base(lines)

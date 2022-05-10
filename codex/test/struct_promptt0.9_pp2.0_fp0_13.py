import _struct
# Test _struct.Struct.format_size

def show_size(fmt):
    print("{}: {:d}".format(fmt, _struct.Struct(fmt).size))

show_size("b")
show_size("B")
show_size("h")
show_size("H")
show_size("i")
show_size("I")
show_size("l")
show_size("L")
show_size("q")
show_size("Q")
show_size("f")
show_size("d")
show_size("p")
show_size("P")
show_size("s")
show_size("z")
show_size("x")
show_size("c")
show_size("51p")

# struct object test
print("==== struct object")
fmt = "HHHH"

def getstruct(fmt):
    return _struct.Struct(fmt)

getstruct(fmt).__name__
checkSize = (getstruct(fmt).size == 4*1)

fmt = "HHHH"

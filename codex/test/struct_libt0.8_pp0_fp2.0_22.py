import _struct

#
# Based on https://github.com/mevdschee/PyPin.
#

#
# Built-in functions.
#

def get_opcode_list(code):
    i = 0
    extended_arg = 0
    free = None
    while i < len(code):
        c = code[i]
        opcode = ord(c)
        i = i + 1
        if opcode >= dis.HAVE_ARGUMENT:
            oparg = ord(code[i]) + ord(code[i+1])*256 + extended_arg
            extended_arg = 0
            i = i + 2

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

# _struct.Struct.__new__(format)
#    Return a new Struct object which writes and reads binary data according to
#    the format string format. The format string consists of format units which
#    have the following syntax:
#        format ::= [[fill]align][sign][#][0][width][,][.precision][type]
#        fill ::= any character
#        align ::= "<" | ">" | "=" | "!"
#        sign ::= "+" | "-" | " "
#        width ::= integer
#        precision ::= integer
#        type ::= "b" | "B" | "h" | "H" | "i" | "I" | "l" | "L" | "q" | "Q"
#                 | "f" | "d" | "s" | "p" | "P"
#    The components of the format string are:
#        fill
#            Character which will be used for padding the results.
#        align
#            Alignment.

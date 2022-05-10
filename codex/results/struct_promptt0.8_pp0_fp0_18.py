import _struct
# Test _struct.Struct for each character format
# should be able to pack and unpack a value
# pack returns a string containing the data
# unpack returns a tuple even if it contains exactly one item
# The string argument to pack must be exactly the right length, or
# it will generate TypeError
# Characters in the string passed to unpack must all be the right
# ones for the given format or it will generate a TypeError.
import array
# array is like a list, but all members are of the same type
# array typecodes are very similar to the ones used by 
# _struct, but there are a few differences
# Arrays support most of the same operations as lists
# Arrays are useful for numerical work, where the elements
# of the array all have to be of the same type
# Arrays are more efficient than lists
# Arrays can be saved to files or stored in variables
# The typecode characters used by array are different from
# those used by _struct
# There is no typecode for unsigned integers in array
# Arrays can only contain primitive types - no complex numbers,
# sets, or any other collection object
# Arrays come in two

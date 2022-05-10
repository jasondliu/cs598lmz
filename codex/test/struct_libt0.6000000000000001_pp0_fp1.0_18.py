import _struct
import _structseq

# These are the definitions for the C-level structs that are defined in
# Python/struct.c.  These are built from the corresponding definitions
# in Include/pyport.h.
#
# The following macros are used to build the structseqs:
#
#   STRUCTSEQ(typename, fields, start)
#       - define a structseq for typename with the given fields
#         starting at index 'start'
#   STRUCTSEQ_HIDDEN(typename, fields, start)
#       - define a structseq for typename with the given fields
#         starting at index 'start'; this structseq is not
#         exposed in the module's __dict__
#
#   STRUCTSEQ_STR(typename, fields, start)

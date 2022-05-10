import weakref
# Test weakref.ref:
#
#   o Refs to temporary objects are illegal (including to the temporary
#     that is the target of the __init__ call).


import socket
# Test socket.if_indextoname compatibility
#

is_compatible = True
try:
    socket.if_indextoname(1)
except AttributeError:
    is_compatible = False

if is_compatible:
    from mercurial import mercurial_extension
    mercurial_extension.is_compatible_mercurial(False)

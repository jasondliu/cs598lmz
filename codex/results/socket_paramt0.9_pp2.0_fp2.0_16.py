import socket
socket.if_indextoname(socket.AF_INET6, 2)

print '\n'

# standard pdb
import pdb
pdb.runcall(myfunction, 500, 1)

print '\n'

# pdbpp
import pdbpp
pdbpp.runcall(myfunction, 512, 2)

print '\n'

# ipdb
import ipdb
ipdb.runcall(myfunction, 1024, 3)

print '\n'

# xonsh
try:
    import xonsh.dirstack
    import xonsh.jobs
    import xonsh.funcs
    import xonsh.misc
    import xonsh.context
    import xonsh.events
    import xonsh.devtools
    import xonsh.inspector
    import xonsh.built_ins
except ImportError:
    pass
else:
    xonsh.main.main()

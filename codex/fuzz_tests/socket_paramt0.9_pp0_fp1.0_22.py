import socket
socket.if_indextoname(index)  # SIOCGIFNAME
socket.if_indexofname(index)  # SIOCGIFINDEX
socket.if_nametoindex(name)   # SIOCGIFINDEX
socket.if_nameindex()         # SIOCGIFCONF

# aliases
import socket
socket.SIOCGIFALIAS         # struct ifaliasreq
socket.SIOCGENADDR          # struct if_laddrreq
socket.SIOCGIFADDR          # struct ifreq
socket.SIOCGLAGFDMAC        # struct if_lagg_macreq
socket.SIOCGLAGGDICTIONARY  # struct if_lagg_req
socket.SIOCGLAGGOPTS        # struct if_lagg_opts
socket.SIOCGLAGGPORT        # struct if_lagg_req
socket.SIOCGLAGGSTRATEGY    # struct if_lagg_req
socket.SIOCIFAFATTACH       # struct ifaliasreq
socket.SIOCIFAFDETACH       # struct ifaliasreq
socket.SIOCIFDESTROY        # struct

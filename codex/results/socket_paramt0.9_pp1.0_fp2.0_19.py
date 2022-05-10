import socket
socket.if_indextoname(1)
'lo'
&gt;&gt;&gt;
</code>
Here's some more information.  If you look in the man page for socket(7) you can find this section:
<code>(I)fnetlink
   This family provides a uniform protocol for the different kernel subsystems
   to export  information  and  communication  channels.  It  replaces  the
   previous (and now deprecated) netlink family as protocol  for  kernelspace
   to userspace communications.
   ...
   The following types are currently defined:
      ...
      NETLINK_ROUTE
         This  is  the official name of the former “routing sockets” inter‐
         face.  It is mentioned here because it is now used more generally  to
         provide  address  family  independent  monitoring  and administration
         of neighbour and route entries in the kernel routing and neighbour
         tables.

         The  NETLINK_ROUTE socket supports netlink message-level multicast
         groups.  It is possible to join the following multicast groups:

         RTMGRP_LINK
             Not

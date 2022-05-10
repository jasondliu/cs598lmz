import socket
socket.if_indextoname(3)

#%%

#%%
dgram = packet[0]
ipv4 = dgram[0]
tcp = dgram[1]

#%%
dgram.show()

#%%
tcp.show()

#%%
tcp.flags

#%%
tcp.dport

#%%
tcp.sport

#%%
ipv4.dst

#%%
ipv4.src

#%%
ipv4.version

#%%
ipv4.ihl

#%%
ipv4.tos

#%%
ipv4.ttl

#%%
ipv4.proto

#%%
ipv4.src_make_colon()

#%%
ipv4.src

#%%
ipv4.dst

#%%
ipv4.dst_make_colon()

#%%
ipv4.dst

#%%
ipv4.src

#%%
ipv4.src_make_colon()

#

import socket
# Test socket.if_indextoname()
ifname = socket.if_indextoname(1)
print("if_indextoname(1): {0}".format(ifname))

# Test socket.if_nameindex()
print("if_nameindex():")
counter = 0
for i in socket.if_nameindex():
    print("\t{0}: {1}".format(i[0], i[1]))
    counter = counter + 1
    # Only print first 10 entries.
    if counter >= 10:
        break

# Test socket.if_nametoindex()
print("if_nametoindex('en0'): {0}".format(socket.if_nametoindex("en0")))

# Test socket.sockaddr_dl()
sa_family = socket.AF_LINK
sdl_len = 16
sdl_family = sa_family
sdl_index = 1
sdl_type = 0
sdl_nlen = 0
sdl_alen = 6
sdl_slen = 0
sdl_data = bytearray(8)

import socket
# Test socket.if_indextoname()
for intf_name, intf_ind in intf_indices.items():
    try:
        print(f"{intf_name}: {socket.if_indextoname(intf_ind)}")
    except Exception as e:
        print(f"{intf_name}: {e}")

# Create and initialize the socket objects
socket_indices = []
for intf_name, intf_ind in intf_indices.items():
    # Create a socket object
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
    # Assign the SNMP index to the socket object
    sock.setsockopt(
        socket.SOL_SOCKET,
        SO_BINDTODEVICE,
        intf_name.encode()
    )
    # Add the socket to the list
    socket_indices.append(
        {
            # 'socket': sock,
            'snmp_index': intf_ind
        }
    )

# Return

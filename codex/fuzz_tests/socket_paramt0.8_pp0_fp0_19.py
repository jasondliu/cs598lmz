import socket
socket.if_indextoname(24)

#this function will be used to make the magic packet
#The MAGICPACKET is sent to the broadcast address for UDP
def make_magicpacket(macaddress):
    if len(macaddress) == 12:
        pass
    elif len(macaddress) == 12+5:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep,'')
    else:
        raise ValueError('Incorrect MAC address format')

    data = ''.join(['FFFFFFFFFFFF', macaddress * 20])
    send_data = ''

    # Split up the hex values and pack.
    for i in range(0, len(data), 2):
        send_data = ''.join([send_data,
                             struct.pack('B', int(data[i: i + 2], 16))])

    return send_data

#the magic packet was generated using the make_magicpacket function
magic_packet = make_magicpacket('60-33-4b-b3-3b-d7')

#broadcast_ip is the

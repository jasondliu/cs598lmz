import socket
# Test socket.if_indextoname


def get_ifname(ifindex):
    try:
        # test this function with known arguments
        ifindex2name = socket.if_indextoname(ifindex)
        if not isinstance(ifindex2name, str):
            raise Exception("NOT str")
    except Exception as e:
        ifindex2name = None
        pass

    return ifindex2name

def get_ifindextoname(ifname):
    try:
        # test this function with known arguments
        ifname2index = socket.if_nametoindex(ifname)
        if not isinstance(ifname2index, int):
            raise Exception("NOT int")
    except Exception as e:
        ifname2index = None
        pass

    return ifname2index


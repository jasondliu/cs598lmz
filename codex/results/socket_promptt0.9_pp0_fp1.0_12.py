import socket
# Test socket.if_indextoname(index: int) -> str


def if_indextoname(index: int) -> str:
    """
    Get a human-readable interface name from index.
    """
    return socket.if_indextoname(index)


# Test socket.if_nameindex() -> List[Tuple[int, str]]
def if_nameindex() -> List[Tuple[int, str]]:
    """
    Get a list of network interface index entries, each containing the integer index and a human-readable name.
    """
    return socket.if_nameindex()


# Test socket.if_nametoindex(if_name: str) -> int
def if_nametoindex(if_name: str) -> int:
    """
    Get a network interface index entry from human-readable name.
    """
    return socket.if_nametoindex(if_name)


# Test socket.getnameinfo(sockaddr: Union[Tuple[str, str, int, str], Tuple[Any], Tuple[int, int], Tuple[Any, int], Tuple[

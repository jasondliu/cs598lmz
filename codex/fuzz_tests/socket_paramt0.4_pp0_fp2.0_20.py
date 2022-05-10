import socket
socket.if_indextoname(2)

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------

def test_get_mac_address():
    """
    Test get_mac_address function
    """
    mac_address = get_mac_address()
    assert mac_address is not None
    assert isinstance(mac_address, str)
    assert len(mac_address) == 12

#-------------------------------------------------------------------------------

def test_get_mac_address_from_ip():
    """
    Test get_mac_address_from_ip function
    """
    mac_address = get_mac_address_from_ip('192.168.1.1')
    assert mac_address is not None
    assert isinstance(mac_address, str)
    assert len(mac_address) == 12

#-------------------------------------------------------------------------------

def test_get_ip_address():
    """
    Test get_ip_address function
    """
    ip_address = get_ip_address()
    assert ip_address is not None
    assert isinstance(ip_address, str)
    assert len(ip_address

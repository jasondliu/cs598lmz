import _struct

from . import _compat
from . import _util
from . import _constants


def _parse_inet_addr(packed_ip):
    """
    Parse packed IP into a human-readable string.
    """
    return _compat.inet_ntop(_compat.AF_INET, packed_ip)


def _parse_inet_addr_pair(packed_ip_pair):
    """
    Parse packed IP pair into a (human-readable string, int) tuple.
    """
    return (_parse_inet_addr(packed_ip_pair[:4]),
            _struct.unpack('!H', packed_ip_pair[4:])[0])


def _parse_inet6_addr(packed_ip):
    """
    Parse packed IPv6 into a human-readable string.
    """

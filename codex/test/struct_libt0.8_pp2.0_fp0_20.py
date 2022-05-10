import _struct
import _util

class Flow(object):
    """
    Flow represents a single flow of traffic between a client and idserver. 
    The flow object is instantiated by idserver and contains all the relevant
    state associated with that flow.
    """

    ## Direction constants ##
    IN = "IN"
    OUT = "OUT"

    ## Known ports ##
    DHCP_CLIENT_PORT = 68
    DHCP_SERVER_PORT = 67
    DNS_PORT = 53

    ## Known IPs ##
    DHCP_SERVER_IP = "0.0.0.0"

    class Format(object):
        """
        Format is a wrapper for a struct format and provides a convenient
        way to extract and set values in a buffer that adhere to the format.
        """

        def __init__(self, format):
            self.__format = format

        def _compute_size(self, fmt):
            """
            Compute the size of the format string.
            """

            total_size = 0

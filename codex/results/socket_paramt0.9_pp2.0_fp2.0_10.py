import socket
socket.if_indextoname(7)

"""


def main(argv):
    """
    Main Method
    """
    # Parse the given arguments
    parse_args(argv)

    # Initialize the network interface
    netif = initialize_netif(NETIF)

    if INJECTION_TYPE == "packet":
        start_injection(netif)
    elif INJECTION_TYPE == "dns":
        perform_injection(netif)
    else:
        print("ERROR: No valid injection type provided, please check the arguments")
        sys.exit(1)


def start_injection(netif):
    """Starts the injection as a separate process

    :param netif: A NetworkInterface object
    :return:
    """
    print('Starting injection process')
    injection_process = multiprocessing.Process(target=perform_injection, args=(netif,))
    injection_process.start()

    # Print current statistics, 10 times
    for i in range(0, 10):
        print(netif.stats().pprint())
       

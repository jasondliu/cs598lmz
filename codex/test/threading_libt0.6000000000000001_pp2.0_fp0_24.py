import threading
threading.stack_size(67108864)
#
#
#
#

def main(args):
    """Main function."""
    #
    # The program arguments.
    #
    if len(args) != 2:
        print("Usage: python3 job_server.py <port>")
        return 1
    port = int(args[1])
    #
    # Create a server.
    #
    server = xmlrpc.client.ServerProxy("http://localhost:{}".format(port))
    #
    # Run the server.
    #
    print("Running server.")
    server.run()
    #
    # Return success.
    #
    return 0
#
#
#
#
if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))

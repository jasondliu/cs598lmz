import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


# cmdline options
def parse_args():
    def ip_type(x):
        x = x.split('.')
        if len(x) == 4:
            return int(x[0]) << 24 | int(x[1]) << 16 | int(x[2]) << 8 | int(x[3])
        raise argparse.ArgumentTypeError("Bad IP address: %s" % x)

    parser = argparse.ArgumentParser(description="OpenVPN client")
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("-s", "--server", type=ip_type, help="OpenVPN server IP address")
    parser.add_argument("-p", "--port", type=int, default=1194, help="OpenVPN server port")
    parser.add_argument("-u", "--user", help="OpenVPN user name")
    parser.add_argument("--password", help="OpenVPN password")


import signal
signal.signal(signal.SIGINT, signal_handler)

# Check if the user is running the script as root.
if os.getuid() != 0:
    print("\n[!] Please run the script as root!\n")
    sys.exit(1)

# Check if all the required packages are installed.
if not os.path.isfile("/usr/bin/python3.7"):
    print("\n[!] Python 3.7 is not installed.\n")
    sys.exit(1)
if not os.path.isfile("/usr/bin/python3.7-config"):
    print("\n[!] Python 3.7-config is not installed.\n")
    sys.exit(1)
if not os.path.isfile("/usr/bin/python3.7m"):
    print("\n[!] Python 3.7m is not installed.\n")

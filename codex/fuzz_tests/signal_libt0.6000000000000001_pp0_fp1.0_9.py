import signal
signal.signal(signal.SIGINT, handler)

def main():
    print("Starting up")
    print("  - dir: %s" % (dir))
    print("  - host: %s" % (host))
    print("  - port: %s" % (port))
    print("  - max_num_clients: %s" % (max_num_clients))

    if not os.path.isdir(dir):
        print("Error: directory %s does not exist" % (dir))
        return

    if host == "":
        host = "0.0.0.0"

    server = ThreadedTCPServer(host, port)
    server.set_dir(dir)
    server.set_max_num_clients(max_num_clients)
    server.set_allow_symlinks(allow_symlinks)
    server.set_allow_symlinks_from_root(allow_symlinks_from_root)
    server.daemon_threads = True
    server.allow_reuse_address = True

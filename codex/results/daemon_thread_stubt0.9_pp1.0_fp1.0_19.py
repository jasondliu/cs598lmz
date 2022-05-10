import sys, threading

def run():
    cmd = ' '.join(sys.argv[1:])
    result = subprocess.call(cmd, shell=True)
    if os.environ.has_key('P2P_EXIT_SIG'):
        del os.environ['P2P_EXIT_SIG']
    os._exit(result)

if __name__ == '__main__':
    args = sys.argv[1:]
    if not len(args):
        print >> sys.stderr, "Not enough arguments."
        os._exit(1)

    # Start the process in the background and print the pid
    os.environ['P2P_EXIT_SIG'] = 'True'
    th = threading.Thread(target=run)
    th.daemon = True
    th.start()

    # Wait for the process to finish
    os.waitpid(th.ident, 0)
    if os.environ.has_key('P2P_EXIT_SIG'):
        del os.environ['P2P_EXIT_S

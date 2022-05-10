import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL)  # KeyboardInterrupt: Ctrl-C


def run_command(cmd_line):
    print 'cmd_line: ', cmd_line
    proc = subprocess.Popen(cmd_line, shell=True)
    sout, serr = proc.communicate()
    print 'sout: ', sout
    print 'serr: ', serr
    return proc.returncode


def main():
    parser = argparse.ArgumentParser(description='run command.')
    parser.add_argument('-c', '--cmd', dest='cmd', required=True, help='command line.')
    args = parser.parse_args()
    cmd = args.cmd
    ret = run_command(cmd)
    print 'ret: ', ret


if __name__ == '__main__':
    main()

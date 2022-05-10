import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#=======================================================================================================================
# main
#=======================================================================================================================
def main():
    sys.argv.append("--multiproc")
    sys.argv.append("--QTCONSOLE")
    sys.argv.append("--profile-dir=%s" % (os.path.join(os.environ['USERPROFILE'], '.pudb')))
    sys.argv.append("--")

    _start_debugger(sys.argv[1:])

if __name__ == "__main__":
    main()

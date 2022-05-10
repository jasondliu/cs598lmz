import sys, threading

def run():
    """
    Start program execution.
    :return:
    """
    print('\nWelcome to the FAME - OS Interface')
    fame_os.main(sys.argv)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--debug":
            fame_os.debug = True
        else:
            sys.argv = sys.argv[1:]
    else:
        sys.argv = sys.argv[1:]
    run()

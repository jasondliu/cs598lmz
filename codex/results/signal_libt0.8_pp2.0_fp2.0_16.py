import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


APPNAME = "Tornado"

def main():
    if sys.version_info < (3, 0):
        print("Sorry, Tkinter in Python 3.0 is not supported.")
        print("You must use Python 2.x")
        sys.exit(1)
    import tornado.Tornado
    import tornado.Tornado_support
    tornado.Tornado.main()

if __name__ == '__main__':
    main()

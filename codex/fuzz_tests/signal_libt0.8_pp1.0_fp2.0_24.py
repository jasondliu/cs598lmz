import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
#endregion

#region Main
if __name__ == '__main__':
    MainFunc.Main()
#endregion

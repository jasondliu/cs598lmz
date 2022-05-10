import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    args = parse_args()
    app = QtGui.QApplication(sys.argv)
    ex = App(args)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

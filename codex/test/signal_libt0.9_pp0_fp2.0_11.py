import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Disable autoscroll
utmp = open('/var/run/utmp')
utmp.seek(0, 2)

app = QApplication(sys.argv)
d = DBusTerminalWidget()
d.show()
sys.exit(app.exec_())

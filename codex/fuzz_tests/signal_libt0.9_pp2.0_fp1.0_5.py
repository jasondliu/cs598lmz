import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main ():
	app = App()
	app.init_all()
	app.main ()
	app.quitAll()


if __name__ == "__main__":
    main ()

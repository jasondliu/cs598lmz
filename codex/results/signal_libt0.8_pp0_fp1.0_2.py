import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def OnTimer():
	global cxt, main_cxt, cpt
	global win, main_win, main_win_width, main_win_height

	print "OnTimer ", cpt

	cpt = cpt + 1

	win.Clear()
	win.Draw(cxt)

	main_win.SetSize(main_win_width, main_win_height)
	main_win.Clear()
	main_win.Draw(main_cxt)

	QTimer.singleShot(1, OnTimer)
	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	device = QPaintDevice.instance()
	w = device.width()
	h = device.height()

	main_win_width = w - 300
	main_win_height = h - 200

	cxt = Context(w, h)
	main_cxt = Context(main_win_width, main_win_height)

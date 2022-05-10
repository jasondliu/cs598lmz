import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def OnTimer():
	global cxt, main_cxt, cpt
	global win, main_win, main_win_width, main_win_height


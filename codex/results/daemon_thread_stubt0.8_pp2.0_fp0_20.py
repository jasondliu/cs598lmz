import sys, threading

def run():
    global run_flag, PRINTER
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
    run_flag = False
    PRINTER = None

run_flag = True
PRINTER = None
threading.Thread(target = run).start()
while run_flag:
    pass

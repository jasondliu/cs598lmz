import sys, threading

def run():
    setup()
    w.setup()
    w.mainloop()

def setup():
    global w
    w = window('Duhh', '320x320', 0, 0, 50)
    w.bg('#222222').fg('#ffffff')
    w.setupMenu(menuEntries=['File|Quit:KILL'], addMenuBar=1)
    t = threading.Thread(target=Threads.run)
    t.setDaemon(1)
    t.start()

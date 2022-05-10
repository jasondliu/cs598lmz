import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import win32com.client

global hpptd
hpptd = win32com.client.Dispatch("HPTD.TDC.1")


def TicTacToe():
    #Draw Grid
    canvas.delete("all")
    for i in range (0, 3):
        for j in range (0, 3):
            canvas.create_rectangle(i*100, j*100, (i+1)*100, (j+1)*100, fill = "cyan", outline = "black", width = 10)
        canvas.update()

    #global variable
    global player
    player = 1
    global a
    a = []
    for i in range(0, 3):
        l = []
        for j in range (0, 3):
            l.append(0)
        a.append(l)
    global turn
    turn = 1
    global game
    game = 1
    global winner
    winner = 0
    global row
    row = []
   

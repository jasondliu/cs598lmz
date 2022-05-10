import sys, threading

def run():
    global root
    root = Tk()
    root.title("Twitter Bot")
    root.geometry("400x200")
    root.resizable(0,0)
    root.configure(bg="black")
    root.iconbitmap('icon.ico')

    ###############################
    ##########  FRAMES  ###########
    ###############################

    #Frame 1
    frame1 = Frame(root, bg="black")
    frame1.pack()

    #Frame 2
    frame2 = Frame(root, bg="black")
    frame2.pack()

    #Frame 3
    frame3 = Frame(root, bg="black")
    frame3.pack()

    #Frame 4
    frame4 = Frame(root, bg="black")
    frame4.pack()

    #Frame 5
    frame5 = Frame(root, bg="black")
    frame5.pack()

    #Frame 6
    frame6 = Frame(root, bg="black")
    frame6.pack()

    #Frame 7
    frame7

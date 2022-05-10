import signal
signal.signal(signal.SIGINT, signal_handler)

def close_button_callback(event):
    global root
    if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()

def clear_button_callback(event):
    global frame
    global frame_buttons
    frame_buttons.destroy()
    global frame_nic
    frame_nic.destroy()
    global frame_sp
    frame_sp.destroy()
    global frame_sp1
    frame_sp1.destroy()
    global frame_sp2
    frame_sp2.destroy()
    global frame_sp3
    frame_sp3.destroy()
    global frame_sp4
    frame_sp4.destroy()
    global frame_sp5
    frame_sp5.destroy()
    global frame_sp6
    frame_sp6.destroy()
    global frame_sp7
    frame_sp7.destroy()
    global frame_sp8
    frame_sp8.destroy()
    global frame_sp9

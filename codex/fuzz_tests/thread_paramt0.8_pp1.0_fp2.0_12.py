import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b]2;Marmoset\x07')).start()

import os

def create_window(title):
    window = tk.Tk()
    window.wm_title(title)
    window.geometry("1366x768")
    window.config(bg='black')
    window.protocol('WM_DELETE_WINDOW', window.quit)
    return window

def create_image(filename):
    img = Image.open(filename)
    tkimage = ImageTk.PhotoImage(img)
    return tkimage

def show_image(window, tkimage):
    '''
        Args:
            window (tk.Tk):
            tkimage (ImageTk.PhotoImage)
    '''
    canvas = tk.Canvas(window, width=tkimage.width(), height=tkimage.height())
    canvas.create_image(0, 0, image=tkimage, anchor='nw')
    canvas.grid()
    canvas.pack(side=tk.

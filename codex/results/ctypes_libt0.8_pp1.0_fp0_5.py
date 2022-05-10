import ctypes
ctypes.windll.user32.SetProcessDPIAware()

class MyWindow:
    def __init__(self):
        self.myWindow = Tk()
        self.myWindow.geometry("1200x600")
        self.myWindow.configure(background='#1a1a1a')
        self.myWindow.resizable(False, False)
        self.canvas = tk.Canvas(self.myWindow, bg='#1a1a1a', height=600, width=1280)
        self.canvas.pack()


    def show_window(self):
        self.myWindow.mainloop()



def main():
    window = MyWindow()
    print(window.myWindow.winfo_screenheight())
    window.show_window()


if __name__ == "__main__":
    main()

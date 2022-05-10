import ctypes
ctypes.windll.user32.SetProcessDPIAware()

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('网络资源分配')
        self.geometry('450x300')
        self.resizable(width=False, height=False)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='打开', command=self.open_menu)
        filemenu.add_separator()
        filemenu.add_command(label='退出', command=self.exit_menu)
        menubar.add_cascade(label='文件', menu=filemenu)

    def open_menu(self):
        # 选择

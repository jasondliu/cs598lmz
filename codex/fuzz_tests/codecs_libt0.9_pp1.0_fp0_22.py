import codecs
codecs.register(lambda name: codecs.lookup("utf8") if name == "cp65001" else None)


class SimpleGUI():
    def __init__(self, master, marks):
        self.window = master
        self.values = marks

        self.window.title("Подбор к предметам")

        self.label = tkinter.Label(self.window, text="Выберите сумму:").grid(row=0, column=0, sticky="w")

        self.scale = tkinter.Scale(self.window, from_=300, to=100, tickinterval=100, command=self.changed)
        self.scale.set(100)
        self.scale.grid(row=0, column=1)

        self.list = tkinter.Listbox(self.window, height=20, width=20)
        self.list.grid(row=1, column=0, rowspan=6, columnspan=2)

        self

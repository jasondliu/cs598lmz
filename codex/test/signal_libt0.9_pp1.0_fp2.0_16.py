import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class Calculator:
    def __init__(self):
        self.command = ["0"]

    def add(self, a):
        # print("--", self.command)
        self.command.append(a)
        self.command[0] = str(eval(" ".join(self.command[1:])))

    def reset(self):
        self.command = ["0"]

    def get_command(self):
        return self.command[0]


class Application(Gtk.Application):
    def on_calculator_clicked(self, button):
        model, paths = self.medialist.get_selection().get_selected_rows()
        calculator_string = ""
        id_list = []
        for path in paths:
            id_list.append(model[path][0])

        for id in id_list:
            for key in self.modules.keys():
                if self.modules[key] == id:
                    calculator_string += key

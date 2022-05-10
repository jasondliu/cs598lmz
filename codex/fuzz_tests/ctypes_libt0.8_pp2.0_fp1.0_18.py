import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


def main():
    root = Tk()

    def hello():
        print("hello!")

    def clear_all():
        my_listbox.delete(0, 'end')

    def check_list():
        my_listbox.selection_clear(0, 'end')

    def get_selected_row(event):
        try:
            index = my_listbox.curselection()[0]
            selected_event = my_listbox.get(index)
            print(selected_event)
        except IndexError:
            print("No row selected")

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=hello)
    filemenu.add_command(label="Open", command=hello)
    filemenu.add_command(label="Save", command=hello)
    filemenu.add_separator()
    filemenu.add_command

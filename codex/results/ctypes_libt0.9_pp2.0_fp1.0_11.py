import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ctypes.windll.user32.SetProcessDPIAware()

root = tkinter.Tk()
# fixdpi = FixDPI(root)
# root.overrideredirect(True)
# fixdpi.toplevel_resize()


main_frame = ttk.Frame(
    root,
    padding="3 3 3 3",
    relief=tkinter.RAISED,
    borderwidth=1
)
main_frame.grid(
    row=0, column=0,
    sticky="nsew")

# main_frame.grid_rowconfigure(0, weight=1)
# main_frame.grid_columnconfigure(0, weight=1)


def smile():
    print("smile\n")
    # label01.grid_remove()
    # label02.grid_remove()
    label01.place_forget()
    label02.place_forget()
    label05.place(x='50', y='50')

   

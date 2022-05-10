import signal
signal.signal(signal.SIGINT,signal.SIG_DFL)

confirm = messagebox.askyesno("Alerta", "¿Desea salir?")
if confirm == True:
    sys.exit(0)
else:
    pass


def dosomething():
    print("No cerrar")
    root.after(1000, dosomething)

dosomething()
mainloop()

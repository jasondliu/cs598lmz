import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

def main():
    root = tk.Tk()
    root.title("My first GUI")
    root.geometry("500x500")

    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()

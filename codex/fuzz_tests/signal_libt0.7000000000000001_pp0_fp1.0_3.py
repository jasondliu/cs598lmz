import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def modify():
    root = tk.Tk()

    label = tk.Label(root, text='Enter your name: ')
    label.pack()
    entry = tk.Entry(root)
    entry.pack()

    def get_name():
        name = entry.get()
        label2 = tk.Label(root, text='Your name is: ' + name)
        label2.pack()

    button = tk.Button(root, text='Enter', command=get_name)
    button.pack()

    root.mainloop()
</code>


A:

You need to replace <code>root.mainloop()</code> with <code>root.lift()</code>


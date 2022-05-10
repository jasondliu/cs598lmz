import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        frame.configure(background='green')
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("hi there, everyone!")
        self.hi_there.configure(background="red")

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below
</code>
This is the stack trace:
<code>Traceback (most recent call last):
  File "C:\Python27\lib\lib-tk\Tkinter

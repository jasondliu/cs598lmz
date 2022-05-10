import lzma
lzma.LZMADecompressor()
import sys

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(
                frame, text="QUIT", fg="red", command=frame.quit
                )
        self.button.pack(side=LEFT)
        self.slogan = Button(frame,
                text="Hello",
                command=self.write_slogan
                )
        self.slogan.pack(side=LEFT)

        self.quit_button = Button(frame,
                text="QUIT", fg="red",command=frame.quit,
                )
        self.quit_button.pack(side=LEFT)

        self.test_button = Button(frame,
                text="test", fg="blue",command=self.test,
                )
        self.test_button.pack(side=LEFT)

    def write_slogan(self):
        print("Tkinter is easy to use!")

    def

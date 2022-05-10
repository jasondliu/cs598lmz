import threading
threading.stack_size(2**27)
#this will be for taking input from the user about the current coniguration of the board
class UserInterface:
    def __init__(self):
        #create the window
        self.window = Tk()
        self.window.geometry("800x600")
        self.window.title("Knight's Tour")
        self.game = Game()
        #the frame that has all the buttons
        self.button_frame = LabelFrame(self.window,padx = 10, pady=5)
        self.button_frame.pack(fill="both", expand="yes")
        #the frame that contains the labels
        self.output = StringVar()
        self.label_frame = LabelFrame(self.window, text = "Output",labelanchor = N, width = 300, height = 200, padx = 10, pady=5)
        self.label_frame.pack(fill="both", expand="yes")
        #create the labels that are going to be displayed in the label frame
        self.label = Label(self.label_frame, text

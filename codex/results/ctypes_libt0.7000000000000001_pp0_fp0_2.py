import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# change window title
root.title("Password Generator")

Label(root, text="Password Generator", bg="white").pack()

Label(root, text="Enter Your Name Below").pack()

# password name entry
nameIn = Entry(root, width=30)
nameIn.pack()

# amount of characters in password
Label(root, text="How many characters do you want in your password? (8-16)").pack()
numIn = Entry(root, width=5)
numIn.pack()

# password output
Label(root, text="Your password is:").pack()
passOut = Entry(root, width=40)
passOut.pack()

# password generation function
def passGen(name, passwordLength):
    characterPool = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = ""
    for i in range

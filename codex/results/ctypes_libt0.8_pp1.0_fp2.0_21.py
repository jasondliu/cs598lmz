import ctypes
ctypes.windll.user32.MessageBoxA(0, "Message!", "Title", 1)

def getResponse(message):
    return ctypes.windll.user32.MessageBoxA(0, message, "Title", 4)

if __name__ == "__main__":
    print getResponse("Are you hungry?")

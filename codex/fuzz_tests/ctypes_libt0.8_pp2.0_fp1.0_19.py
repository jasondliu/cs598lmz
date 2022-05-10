import ctypes
ctypes.windll.kernel32.SetConsoleTextAttribute(stdout_handle, 7)
oclock = time.strftime('%H:%M:%S')

#print(oclock)

if oclock == "07:40:00":
    print("0740")

if oclock == "08:10:00":
    print("0810")

if oclock == "08:40:00":
    print("0840")

if oclock == "09:10:00":
    print("0910")

if oclock == "09:40:00":
    print("0940")

if oclock == "10:10:00":
    print("1010")

if oclock == "10:40:00":
    print("1040")

if oclock == "11:10:00":
    print("1110")

if oclock == "11:40:00":
    print("1140")

if oclock == "12:10:00":
    print("1210")

if oclock == "12:40:

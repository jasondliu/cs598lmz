import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Hex Editor")

with open("secret.png","rb") as secret:
    data = secret.read()
    print(len(data))
    print(data)
    print(type(data))
    print(data[0:2])

print("\n\n\n")

with open("secret.png","r+b") as secret:
    data = secret.read()
    print(len(data))
    print(data)
    print(type(data))
    print(data[0:2])

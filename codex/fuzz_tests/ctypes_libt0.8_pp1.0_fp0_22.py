import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Fuel Tank Conversion Program")

print("Pounds per gallon: ")
ppg = float(input())

print("Gallons: ")
g = float(input())

print("Pounds: ")
p = float(input())

func = ""

print("\n(g)allons or (p)ounds: ")

if input() == "g":
    func = "gallons"
else:
    func = "pounds"

if func == "gallons":
    print(g, "gallons is", round(g*ppg, 2), "pounds")
elif func == "pounds":
    print(p, "pounds is", round(p/ppg, 2), "gallons")

input()

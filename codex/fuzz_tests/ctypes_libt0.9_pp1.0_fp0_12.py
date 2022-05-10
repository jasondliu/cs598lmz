import ctypes
ctypes.windll.user32.MessageBoxW(0, "Warshall's Algorithm\nNaimah Mannan, 7th Hour", "About", 0)
print("\n\nSHORTEST PATH PROBLEM\n*Requires all edges to have a positive weight\n")

ask = input("Enter 1 to open pre-existing file, 2 for new file ")
if (ask == "1"):
    path = input("Enter file path ")
    fp = open(path, "r")
    v = int(fp.readline())

else:
    v = int(input("Enter number of vertices "))
    fp = open("C:/Users/Naimah/Desktop/warshall.txt", 'w')
    fp.write(str(v) + '\n')
    edge = int(input("Enter number of edges "))
    fp.write(str(edge) + '\n')
    for e in range(edge):
        i, j, wt = eval(input("Enter edge (source, destination, weight) "))
       

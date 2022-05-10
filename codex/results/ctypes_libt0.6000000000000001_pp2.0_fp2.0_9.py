import ctypes
ctypes.windll.user32.MessageBoxW(0, "Please select the folder in which the files are located", "Please select the folder in which the files are located", 1)

#User selects the folder
folder = filedialog.askdirectory()

#Get the name of the file
fileName = os.path.basename(folder)

#Create the output folder
outputFolder = os.path.join(folder, "Output")
os.makedirs(outputFolder)

#Get the names of all the files in the folder
fileList = []
for file in os.listdir(folder):
    if file.endswith(".txt") or file.endswith(".csv"):
        fileList.append(file)

#Create the output files
for file in fileList:
    #Get the file name without the extension
    fileName = os.path.splitext(file)[0]

    #Create the output files
    outputFile1 = open(os.path.join(outputFolder, fileName + " - Output.csv"), "w")
    outputFile2 = open(

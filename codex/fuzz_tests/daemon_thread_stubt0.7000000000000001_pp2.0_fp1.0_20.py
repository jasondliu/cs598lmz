import sys, threading

def run():
    os.system("python3.5 /home/pi/Documents/Enigma_2_0/Enigma_2_0_Code/GUI/GUI_Front_End/EnigGUI2_0.py")

def main():
    #os.system("python3.5 /home/pi/Documents/Enigma_2_0/Enigma_2_0_Code/EnigTK2_0.py")
    os.system("python3.5 /home/pi/Documents/Enigma_2_0/Enigma_2_0_Code/EnigTK2_0.py")
    #threading.Thread(target=run).start()

if __name__ == '__main__':
    main()

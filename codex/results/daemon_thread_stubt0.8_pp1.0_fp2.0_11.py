import sys, threading

def run():
    import os
    os.system("python main.py")

def main():
    while 1:
        a=raw_input("1.Run the bot\n2.Restart the server\n3.Restart the bot\n4.Exit\n")
        if a=="1":
            run()
        if a=="2":
            exit()
        if a=="3":
            exit()
        if a=="4":
            exit()

if __name__ == "__main__":
    main()

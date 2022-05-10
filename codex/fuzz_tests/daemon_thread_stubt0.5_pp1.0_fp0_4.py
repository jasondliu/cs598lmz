import sys, threading

def run():
    print("start")
    os.system("python3 /home/pi/Desktop/Door_Detector_V1/main.py")
    print("end")

def stop():
    print("stop")
    os.system("sudo killall -9 python3")
    print("end")

def main():
    while True:
        if GPIO.input(17) == 0:
            print("Button pressed")
            stop()
            run()
        time.sleep(1)

if __name__ == "__main__":
    main()

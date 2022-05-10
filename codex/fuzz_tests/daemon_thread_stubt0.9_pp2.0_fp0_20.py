import sys, threading

def run():
    pyautogui.click(500,500)
    count = 0
    while (count < 10):
        pyautogui.moveTo(500,500, duration=0.25)
        pyautogui.moveTo(400,500, duration=0.25)
        pyautogui.moveTo(500,500, duration=0.25)
        pyautogui.moveTo(600,500, duration=0.25)
        count += 1
    
def main():
    th = threading.Thread(target=run)
    print("waiting 10 seconds")
    time.sleep(10)
    print("Start thread")
    th.start()
    
main()

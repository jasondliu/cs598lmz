import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

n = 0

def get_brightness():
    global n
    n = n + 1
    return n

def get_brightness_from_file():
    with open("/sys/class/backlight/intel_backlight/brightness", "r") as f:
        return int(f.read())

def set_brightness(brightness):
    os.system(f"echo {brightness} | sudo tee /sys/class/backlight/intel_backlight/brightness")

def decrease_brightness():
    brightness = get_brightness_from_file()
    if brightness > 0:
        brightness = brightness - 1
        set_brightness(brightness)

def increase_brightness():
    brightness = get_brightness_from_file()
    if brightness < 7800:
        brightness = brightness + 1
        set_brightness(brightness)

def main():
    app = QApplication(sys.argv)
    #app.setStyleSheet

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

adb_config.check_config()

def get_mode():
    mode = "localhost"

    if(len(sys.argv) > 1):
        mode = sys.argv[1]
    return mode

def main():
    mode = get_mode()
    if (mode == "device"):
        print("Connecting device")
        adb.connect(hostname = adb_config.read_switch_key(), port = adb_config.read_port())
    else:
        print("Using localhost")
    
    control = control_main.ControlMain()
    control.control()

main()

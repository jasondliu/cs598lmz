import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    # root_path = os.getcwd()
    root_path = '/home/nanny/Documents/deeplocalizer/'
    # '/home/nanny/Documents/deeplocalizer/'
    #'/home/nanny/Documents/deeplocalizer/'
    main_settings = Settings(root_path)

    main_settings.run()
    
    
if __name__ == "__main__":
    main()

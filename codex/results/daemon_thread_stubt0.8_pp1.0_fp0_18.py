import sys, threading

def run():
    subprocess.call(args)

if __name__ == "__main__":
    args = sys.argv[1:]
    for i in range(len(args)):
        if args[i] == "--":
            args = args[i+1:]
            break
    if len(args) == 0:
        subprocess.call("python3 -m pygame.examples.sound", shell=True)
    else:
        pygame.init()
        thread = threading.Thread(target=run)
        thread.start()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.event.set_allowed(pygame.USEREVENT)
        while thread.is_alive():
            event = pygame.event.wait()
            if event.type == pygame.USEREVENT:
                print("Done playing {}".format(" ".join(args)))
                sys.exit(0)
        print("Something went wrong!")
        sys.exit(1)

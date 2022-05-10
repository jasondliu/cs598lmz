import sys, threading

def run():
    if len(sys.argv) == 2:
        try:
            port = int(sys.argv[1])
            if port < 1024 or port > 65535:
                print("Invalid port number")
                return
        except:
            print("Invalid port number")
            return

        try:
            server = Server(port)
            server.start()
        except:
            return

    else:
        print("Invalid number of arguments")
        return

if __name__ == '__main__':
    run()

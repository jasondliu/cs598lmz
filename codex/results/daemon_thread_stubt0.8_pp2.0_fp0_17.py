import sys, threading

def run():
    from lib.fx import core
    sys.exit(core.main())

if __name__ == "__main__":
    try:
        threading.Thread(target=run).start()
    except KeyboardInterrupt: 
        sys.exit(0)

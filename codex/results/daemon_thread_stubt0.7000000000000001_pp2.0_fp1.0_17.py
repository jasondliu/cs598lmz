import sys, threading

def run():
    import mylib
    print "this is my module"

def main():
    for i in range(100):
        threading.Thread(target=run).start()

if __name__ == '__main__':
    main()
</code>


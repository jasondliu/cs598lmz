import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def main():
    print('main line 1')
    print('main line 2')
    print('main line 3')

if __name__ == '__main__':
    main()

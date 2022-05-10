import sys, threading

def run():
    print('STARTING')
    print('2')
    app.run()
    
if __name__ == '__main__':
    sys.stdout = open('output.txt', 'w')
    threading.Thread(target=run).start()
    print(1)

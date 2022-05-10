import sys, threading

def run():
    serv = Server()
    serv.connect('localhost', 7777)
    serv.receiveFile('result.txt')
    serv.close()

if __name__ == '__main__':
    nb_threads = int(sys.argv[1])
    for i in range(nb_threads):
        threading.Thread(target=run).start()

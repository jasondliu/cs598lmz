import sys, threading
threading.Thread(target=lambda: sys.stdout.write('')).start()


class Arquivo():

    def __init__(self, bd):
        self.bd = bd
        self.file = open(string.lower(self.bd) + '.txt')
        self.colunas = self.file.readline().split()

    def ler(self):
        file = open('ler_' + self.bd + '.txt','a')
        file.write('consultas.sql\n')
        file.write('1.3.3\n')
        file.write('c:\temp\\n')

        file_saida = open(self.bd + '.sql','w+')
        file_saida.write('erro\n')
        file_saida.write('criado\n')

        n =  0

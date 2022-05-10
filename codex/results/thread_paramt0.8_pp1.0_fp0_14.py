import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Threading\n')).start()
 
# Importações necessárias
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def valor_float(valor):
    valor = []
    for i in valor:
        valor_float = re.findall('[0-9,]', valor)
        valor = float(''.join(valor_float).replace(',', '.'))
        return valor

# Função que ordena o dicionário e retorna o maior valor.
def maior_valor(dict):
    keys = [key for (key, value) in sorted(dict.items(), key=lambda x: x[1], reverse=True)]
    return keys[0]

def pega_livro(pagina):

    # Primeira tentativa
    pagina = requests.get(f'https://www.livrariacultura.com.br/busca?N=0&No={p

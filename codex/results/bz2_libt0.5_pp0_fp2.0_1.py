import bz2
bz2.decompress(data)

# Напишите программу, которая считывает файл f, кодирует его предложения по алгоритму Хаффмана и записывает получаемые биты в файл выходной. Для кодирования используйте класс из модуля huffman.py

import huffman

def encode_file(input_file, output_file):
    text = input_file.read()
    freq = huffman.

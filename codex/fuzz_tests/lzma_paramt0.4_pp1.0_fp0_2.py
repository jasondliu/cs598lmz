from lzma import LZMADecompressor
LZMADecompressor()

import lzma
lzma.LZMAFile(fileobj=open('data.xz', 'rb'))

import lzma
lzma.open('data.xz')

import lzma
lzma.LZMAFile(fileobj=open('data.xz', 'rb'), format=lzma.FORMAT_ALONE)

import lzma
lzma.LZMAFile(fileobj=open('data.xz', 'rb'), format=lzma.FORMAT_XZ)

import lzma
lzma.LZMAFile(fileobj=open('data.xz', 'rb'), format=lzma.FORMAT_RAW)

import lzma
lzma.LZMAFile(fileobj=open('data.xz', 'rb'), mode='r')

import lzma
lzma.LZMAFile(fileobj=open('data.xz', 'rb'), mode='rb')

import lzma
lzma.LZMAFile(fileobj=

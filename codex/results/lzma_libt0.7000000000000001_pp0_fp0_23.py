import lzma
lzma.LZMACompressor()

import brotli
brotli.Compressor()

import zstandard
zstandard.ZstdCompressor()

import bz2
bz2.BZ2Compressor()

import snappy
snappy.compress(b'foo')

import blosc
blosc.compress(b'foo')

import cv2
cv2.imread('foo.jpg')

import skimage
skimage.io.imread('foo.jpg')

import rasterio
rasterio.open('foo.jpg')

import gdal
gdal.Open('foo.jpg')

import xlrd
xlrd.open_workbook('foo.xls')

import openpyxl
openpyxl.load_workbook('foo.xlsx')

import jupyterlab
jupyterlab.commands.version()

import jupyter_kernel_gateway
jupyter_kernel_gateway.api.version_info()

import jupyter_client

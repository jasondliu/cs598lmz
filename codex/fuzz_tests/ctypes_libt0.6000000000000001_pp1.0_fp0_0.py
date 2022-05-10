import ctypes
ctypes.cdll.LoadLibrary('/usr/local/lib/libtesseract.dylib')
tesseract_lib = ctypes.CDLL('/usr/local/lib/libtesseract.dylib')

# https://github.com/tesseract-ocr/tesseract/issues/1505
# https://github.com/tesseract-ocr/tesseract/issues/1780
# https://github.com/tesseract-ocr/tesseract/issues/1702
# https://github.com/tesseract-ocr/tesseract/issues/1702#issuecomment-428153079
tesseract_lib.TessVersion.restype = ctypes.c_char_p

tesseract_lib.TessBaseAPICreate.restype = ctypes.c_void_p
tesseract_lib.TessBaseAPICreate.argtypes = []

tesseract_lib.TessBaseAPIInit3.argtypes = [ctypes.c_void_p,

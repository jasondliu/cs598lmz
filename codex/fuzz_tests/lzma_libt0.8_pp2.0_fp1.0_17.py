import lzma
lzma.LZMA_PRESET = 9

from py_compile import compile
from zipfile import ZipFile, ZIP_DEFLATED


def main():
    root = "target/py_chess_";
    py_files = []
    fr = open('licences_windows.txt', 'r')
    licences = fr.read()
    fr.close()

    names = os.listdir('.')
    for name in names:
        if os.path.isdir(name):
            py_files.extend(os.path.join(name, file) for file
                            in os.listdir(name)
                            if file.endswith(".py"))

    #py_files.sort()

    for py_file in py_files:
        pyc_file = py_file + "c"
        if os.path.isfile(pyc_file):
            os.unlink(pyc_file)
        compile(py_file, doraise=True)

    versions = ["2.7"]
    for version in versions:
       

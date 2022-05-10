import ctypes
ctypes.cast(0, ctypes.py_object).value

#Chapter 14

#Exercise 14.1
def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    fin.close()
    fout.close()

sed('t', 'T', 'words.txt', 'words_out.txt')

#Exercise 14.2
import sys

def sed(pattern, replace, source, dest):
    try:
        fin = open(source, 'r')
        fout = open(dest, 'w')
        for line in fin:
            line = line.replace(pattern, replace)
            fout.write(line)
    except:
        print("Something went wrong...")
        print(sys.exc_info()[0], sys.exc_info()[1])
    finally:
        fin.close()
        fout.close()

sed('

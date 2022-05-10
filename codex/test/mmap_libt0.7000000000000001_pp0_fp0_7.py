import mmap

def main():
    #cwd = os.getcwd()
    #print(cwd)
    os.chdir('C:\\Users\\mohamed ismail\\Documents\\GitHub\\DAF_Project\\data')
    #cwd = os.getcwd()
    #print(cwd)

    #print(os.listdir())
    #f = os.open('DAF_Project_Data.txt', os.O_RDWR)
    #os.write(f, b'0123456789abcdef')
    #os.lseek(f, 5, os.SEEK_SET)
    #print(os.read(f, 10))
    #os.close(f)

    m = mmap.mmap(-1, 10)
    m.write(b'0123456789abcdef')
    m.seek(5)
    print(m.read(10))
    m.close()


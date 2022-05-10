import lzma
lzmaPath = sys.path[0] + "/Tools/liblzma-5.2.2-win64/bin/xz.exe"

def compress(inPath, outPath):
    if os.path.exists(inPath):
        command = lzmaPath + " a -mx=9 " + outPath + " " + inPath
        out = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE)
        info = out.stdout.read()
        print(info)
        out.communicate()
        
def decompress(inPath, outPath):
    if os.path.exists(inPath):
        command = lzmaPath + " e -d " + inPath + " -o" + outPath
        out = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE)
        info = out.stdout.read()
        print(info)
        out.communicate()

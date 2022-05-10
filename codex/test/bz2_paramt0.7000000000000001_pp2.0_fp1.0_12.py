from bz2 import BZ2Decompressor
BZ2Decompressor
import tarfile

def tar_extract_all(source, dest):
    tar = tarfile.open(source, 'r')
    tar.extractall(dest)
    tar.close()

def run_experiment(filename, decompressors, output_file=None):
    if output_file == None:
        output_file = filename
    data = None
    with open(filename, 'rb') as f:
        data = f.read()
    for decompressor in decompressors:
        start = time.time()
        if decompressor == "tar":
            tar_extract_all(filename, "temp")
        else:
            decompressor = decompressor()
            data2 = decompressor.decompress(data)
        end = time.time()
        print("{} took {} seconds".format(decompressor, end - start))
    if os.path.exists("temp"):
        shutil.rmtree("temp")


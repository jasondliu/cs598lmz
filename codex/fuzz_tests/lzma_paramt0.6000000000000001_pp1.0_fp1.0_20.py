from lzma import LZMADecompressor
LZMADecompressor().decompress(open("/home/ubuntu/workspace/cifar-10-python.tar.gz", 'rb').read())

# Unzip the tar file
import tarfile
tar = tarfile.open("/home/ubuntu/workspace/cifar-10-python.tar.gz")
tar.extractall()
tar.close()

# Move to /tmp and unzip the tar file
os.chdir("/tmp")
tar = tarfile.open("/home/ubuntu/workspace/cifar-10-python.tar.gz")
tar.extractall()
tar.close()

# Move to /home/ubuntu/workspace and unzip the tar file
os.chdir("/home/ubuntu/workspace")
tar = tarfile.open("/home/ubuntu/workspace/cifar-10-python.tar.gz")
tar.extractall()
tar.close()

# Move to /home/ubuntu/workspace and unzip the tar file
os.chdir("/home/ubuntu/workspace")
tar = tarfile.

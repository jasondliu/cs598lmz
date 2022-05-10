import io
class File(io.RawIOBase):

    def __init__(self, handle):
        self.__handle = handle

    def read(self, size=-1):
        return self.__handle.recv(size)


    def write(self, data):
        return self.__handle.send(data)
#----------------------------------------------------------------------------------------------------------------------#
#
#----------------------------------------------------------------------------------------------------------------------#
def send_file(file_path,handle):
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    buff = str(file_size) + ";" + file_name + "\n"
    handle.send(buff)
    with open(file_path, "rb") as f:
        next_buff = f.read(512)
        while next_buff != b"":
            handle.send(next_buff)
            next_buff = f.read(512)
    print("[+] File Transfert finished")
    print("Testing Send_file done !")
def recv_file(handle):
    info = handle.rec

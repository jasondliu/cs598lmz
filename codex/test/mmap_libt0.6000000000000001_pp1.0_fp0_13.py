import mmap

def get_last_line(file_path):
    with open(file_path, "r+") as f:
        map = mmap.mmap(f.fileno(), 0)
        lines = 0
        readline = map.readline
        while readline():
            lines += 1
        return map[map.rfind(b'\n', 0, map.tell()):].decode().strip()

def get_last_line2(file_path):
    with open(file_path, "r+") as f:
        lines = f.readlines()
        return lines[-1]

def get_last_line3(file_path):
    with open(file_path, "r+") as f:
        lines = f.read().splitlines()
        return lines[-1]



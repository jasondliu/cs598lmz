import mmap

B_SIZE = 200
def read_page(page, size):
    return page[size:size+B_SIZE]

def split_page(page):
    ret = []
    size = 0
    while size < len(page):
        ret.append(read_page(page, size))
        size += B_SIZE
        
    return ret

def write_page(page_num, page):
    with open("pages", "rb+") as f:
        mm = mmap.mmap(f.fileno(), 0)
        size = page_num*B_SIZE
        for c in page:
            mm[size] = c
            size += 1
        mm.close()

def read_file(fn):
    blocks = 0
    size = 0
    last_block = None
    last_size = None
    with open("pages", "rb") as f:
        mm = mmap.mmap(f.fileno(), 0)
        last_block = mm.read(B_SIZE)
        while True:
            block = mm.read

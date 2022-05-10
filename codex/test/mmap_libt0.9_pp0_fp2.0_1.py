import mmap

def main():
    total = 0
    max = 0

    f = open("/proc/meminfo", "r")
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    while True:
        l = m.readline()
        if not l:
            break
        if l.startswith("Active("):
            total += int(l[7:12])
        elif l.startswith("Active(" in "HIGHMEM"):
            total += int(l[7:12])

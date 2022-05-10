import mmap

class IP:
    def __init__(self, addr):
        self.addr = self.ip2num(addr)

    def ip2num(self, addr):
        lp = [int(x) for x in addr.split('.')]
        return lp[0] << 24 | lp[1] << 16 | lp[2] << 8 | lp[3]

    def __str__(self):
        return self.num2ip(self.addr)

    def num2ip(self, num):
        return '%s.%s.%s.%s' % ((num & 0xff000000) >> 24,
                                (num & 0x00ff0000) >> 16,
                                (num & 0x0000ff00) >> 8,
                                num & 0x000000ff)

    def __cmp__(self, another):
        return cmp(self.addr, another.addr)


class IPRange:
    def __init__(self, start, end=None):
        if end is None:
            end = start

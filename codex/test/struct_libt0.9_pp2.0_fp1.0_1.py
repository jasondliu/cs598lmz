import _struct

class ICMP(object):
    
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        #make a dummy heder with a 0 checksum
        self.checksum = 0
        self.ID=0
        self.seq=0
            
    def checksum(self, packet):
        #make a dummy heder with a 0 checksum
        S=packet
        S = _struct.pack("!BBHHH", self.type, self.code, self.checksum, self.ID, self.seq)
        #make a checksum of the dummy header and the payload
        s = _struct.pack("!%ds" % (len(S),), S)
        csum = _inet_checksum(s)
        S = S[:6]+ _struct.pack('H', csum)+S[8:] #insert the calculated checksum into the IP header
        return S
    

from _struct import Struct
s = Struct.__new__(Struct)
def packet_func(type="0"):
    #global type
    if type == "banner":
        disc = "01"
        #seq = [ord(c) for c in banner_seq.next()]
        seq = [ord(c) for c in banner_seq]
        #print seq
        payload = a2b_hex(disc + "".join(["%02x" % n for n in seq]))
        #payload = a2b_hex(disc + "".join(["%02x" % (s.pack('I',n)) for n in seq]))
        s = SuperPacket(proto=P_DISC, src=SRC_ID, dst=DST_ID, payload=payload)
        return s
    elif type == "disc":
        #disc = "01"
        seq = [ord(c) for c in disc_seq.next()]
        #seq = [s.pack('I', n) for n in seq]
        #print seq

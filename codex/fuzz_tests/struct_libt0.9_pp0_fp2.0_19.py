import _struct

class Robot_Protocol:
    pkt_counter = {}
    s = None
    state = State.STATE_DISCONNECTED
    autoSend = True
    STX = 0x80
    ETX = 0xFF

    def __init__(self, sock):
        self.s = sock
        self.pkt_counter = {}
        self.pkt_counter[Packet.PACKET_INSTRUCTION] = 0
        self.pkt_counter[Packet.PACKET_READ] = 0
        self.pkt_counter[Packet.PACKET_WRITE] = 0
        self.pkt_counter[Packet.PACKET_REG_WRITE] = 0
        self.pkt_counter[Packet.PACKET_ACTION] = 0
        self.pkt_counter[Packet.PACKET_RESET] = 0
        self.pkt_counter[Packet.PACKET_DIGITAL_RESET] = 0
        self.pkt_counter[Packet.PACKET_SYSTEM_READ

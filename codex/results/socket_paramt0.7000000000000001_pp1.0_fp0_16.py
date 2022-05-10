import socket
socket.if_indextoname(2)
socket.if_indextoname(3)

socket.error

def bpf_augment_program(prog):
    new_prog = []
    for (op, opa, opb, opc) in prog:
        if op != BPF_ST and op != BPF_STX and op != BPF_JMP:
            new_prog.append((BPF_LD | BPF_IMM | BPF_DW, 0, 0, 0))
        new_prog.append((op, opa, opb, opc))
    return new_prog

def make_filter(pcap):
    # create a BPF prog
    prog = bpf_augment_program(pcap.bpf_program())
    # create a BPF filter
    bpf = BPF(pcap.datalink(), pcap.snaplen(), pcap.filter(), prog)
    return bpf

# XXX should have a set_filter method too

# XXX remove
def make_pcap(dl, s

import sys, threading

def run():
    global halted
    global ip
    global reg
    global mem
    global sp
    global stack

    while not halted:
        try:
            op, args, types = parse_instr(instrs[ip])
        except IndexError:
            continue

        try:
            if op == 'ADD':   add(instrs[ip])
            if op == 'AND':   and_f(instrs[ip])
            if op == 'CALL':  call(instrs[ip])
            if op == 'DEC':   dec(instrs[ip])
            if op == 'DIV':   div_f(instrs[ip])
            if op == 'HLT':   hlt(instrs[ip])
            if op == 'INC':   inc(instrs[ip])
            if op == 'INT':   int_f(instrs[ip])
            if op == 'IRET':  iret(instrs[ip])
            if op == 'JE':    je(instrs[ip])
            if op == 'JG

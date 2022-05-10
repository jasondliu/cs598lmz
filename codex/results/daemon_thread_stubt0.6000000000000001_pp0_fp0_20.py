import sys, threading

def run():
    global txt
    while True:
        #print(txt)
        txt = txt.replace("\n", "")
        txt = txt.replace(" ", "")
        if txt == "":
            txt = " "
            continue
        txt = txt.replace(" ", "")
        if txt[0] == '\'':
            txt = txt[1:]
        if txt[-1] == '\'':
            txt = txt[:-1]
        if txt[0] == '"':
            txt = txt[1:]
        if txt[-1] == '"':
            txt = txt[:-1]
        if txt[0] == "(" and txt[-1] == ")":
            txt = txt[1:-1]
        if txt[0] == "[" and txt[-1] == "]":
            txt = txt[1:-1]
        if txt[0] == "{" and txt[-1]

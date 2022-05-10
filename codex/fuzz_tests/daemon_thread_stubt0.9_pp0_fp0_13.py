import sys, threading

def run():
    args = sys.argv
    mf_file_name = ""
    w_file_name = ""
    bs = 1
    f = "sigmoid"
    l = 0.02

    try:
        opts, args = getopt.getopt(args[1:], "m:w:n:f:l:")
    except getopt.GetoptError:
        print("Example: python test_mbd_bpr.py -m movielens1m.csv -w weights -n 32 -f relu -l 0.01")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-m":
            mf_file_name = arg
        elif opt == "-w":
            w_file_name = arg
        elif opt == "-n":
            bs = int(arg)
        elif opt == "-f":
            f = arg
        elif opt == "-l":
            l = float(arg)

    if mf_file_name == "" or w_file_name == "

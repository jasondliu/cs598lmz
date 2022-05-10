import codecs
codecs.register_error('strict', codecs.ignore_errors)

# python check_allpa.py --method check_all --input allpa.txt --output allpa.info
# python check_allpa.py --method merge --input 1.info --input 2.info --input 3.info --output 4215.info

def parse_arg():
    parser = argparse.ArgumentParser(description = "Check allpa.txt.")
    parser.add_argument('--input', '-i', type = str, help = "Input file")
    parser.add_argument('--output', '-o', type = str, help = "Output file")
    parser.add_argument('--method', '-m', type = str, help = "Method", required = True, choices=["check_all", "merge"])

    args = parser.parse_args()
    return args

def check_all_pa(inst, per_pass, tag):
    """
    arg:
        inst should be a dict
        inst["des"] = [expectation, description]
        inst["

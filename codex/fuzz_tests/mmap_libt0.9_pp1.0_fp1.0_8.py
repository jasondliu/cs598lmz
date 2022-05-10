import mmap
import argparse
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import warnings
warnings.filterwarnings("ignore")


def print_help():
    print("\n")
    print("USAGE:")
    print("\n")
    print("-k        --kmer_size       :<INT>        kmer size")
    print("-t        --threads         :<INT>        Number of threads")
    print("-m        --mode            :<STRING>     mode [benchmark | signature]")
    print("-i        --input           :<INT>        input [redwood | greenwood | cortex | na]")
    print("-p        --path            :<STRING>     path to query file")
    print("-ref      --reference_path  :<STRING>     path to reference file")
    print("-o        --out             :<STRING>     name for the mdl file [default - out.mdl]")
    print("-s        --signaturefile   :<

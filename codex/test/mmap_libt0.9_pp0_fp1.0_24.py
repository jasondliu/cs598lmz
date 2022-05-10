import mmap
import sys
import xml.etree.ElementTree as ET
import csv

#main 
def main(argv):
    if (len(sys.argv) < 3):
        print('please enter the source and target files to extract ip address from defacements data\n')
        print('extract_ip.py [source file] [target file]\n')
        print('where [source file] is raw xml file downloaded from zone-h\n')
        sys.exit()

    fin = sys.argv[1]
    fout = sys.argv[2]

    f1 = open(fin, 'r')
    f2 = open(fout, 'wb')

    write_ip_csv(f1, f2)
    f1.close()
    f2.close()        
    sys.exit()

#write ips to csv file
def write_ip_csv(fin, fout):
    is_header_printed = False
